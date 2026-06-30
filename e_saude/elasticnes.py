from __future__ import annotations

import csv
import json
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .schema import ADDRESS_FIELDS


ELASTICNES_BASE_URL = "https://elasticnes.saude.gov.br"
ELASTICNES_INDEX = "cgsi-cnesprod-c1*"
ELASTICNES_SEARCH_URL = f"{ELASTICNES_BASE_URL}/kibana/internal/search/es"

SOURCE_FIELDS = [
    "LOGRADOURO",
    "COMPLEMENTO DO ENDEREÇO",
    "BAIRRO",
    "MUNICÍPIO",
    "UF",
    "CEP",
]


class ElasticnesError(RuntimeError):
    """Erro ao consultar dados públicos do ElastiCNES."""


def download_elasticnes_addresses(
    output: Path,
    limit: int = 1_000,
    uf: str | None = None,
    competencia: str | None = "202605",
    timeout: int = 30,
    page_size: int = 500,
    sleep_seconds: float = 0.2,
) -> int:
    """Baixa endereços públicos do ElastiCNES para um CSV de cache."""

    output.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    offset = 0

    with output.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=ADDRESS_FIELDS, delimiter=";")
        writer.writeheader()

        while total < limit:
            batch_size = min(page_size, limit - total)
            payload = _build_payload(batch_size, uf, competencia, offset)
            response = _post_json(ELASTICNES_SEARCH_URL, payload, timeout)
            hits = _extract_hits(response)
            if not hits:
                break

            for hit in hits:
                writer.writerow(_normalize_address(hit.get("_source", {})))
                total += 1

            offset += len(hits)
            time.sleep(sleep_seconds)

    return total


def _build_payload(
    size: int,
    uf: str | None,
    competencia: str | None,
    offset: int,
) -> dict[str, Any]:
    filters: list[dict[str, Any]] = [
        {"term": {"STATUS DO ESTABELECIMENTO.keyword": "ATIVO"}},
    ]
    if uf:
        filters.append({"term": {"UF.keyword": uf.upper()}})
    if competencia:
        filters.append({"term": {"index_comp.keyword": competencia}})

    body: dict[str, Any] = {
        "size": size,
        "from": offset,
        "_source": SOURCE_FIELDS,
        "query": {"bool": {"filter": filters}},
        "sort": [{"CNES.keyword": "asc"}],
    }
    return {
        "params": {
            "index": ELASTICNES_INDEX,
            "body": body,
        }
    }


def _post_json(url: str, payload: dict[str, Any], timeout: int) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "kbn-xsrf": "true",
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as error:
        message = error.read().decode("utf-8", errors="replace")
        raise ElasticnesError(f"ElastiCNES retornou HTTP {error.code}: {message}") from error
    except (URLError, TimeoutError) as error:
        raise ElasticnesError(f"Falha ao acessar o ElastiCNES: {error}") from error


def _extract_hits(response: dict[str, Any]) -> list[dict[str, Any]]:
    raw_response = response.get("rawResponse", response)
    hits = raw_response.get("hits", {}).get("hits", [])
    if not isinstance(hits, list):
        return []
    return hits


def _normalize_address(source: dict[str, Any]) -> dict[str, str]:
    return {
        "LOGRADOURO": str(source.get("LOGRADOURO") or "").strip(),
        "NUMERO": "",
        "COMPLEMENTO": str(source.get("COMPLEMENTO DO ENDEREÇO") or "N/A").strip(),
        "BAIRRO": str(source.get("BAIRRO") or "").strip(),
        "MUNICIPIO": str(source.get("MUNICÍPIO") or "").strip(),
        "UF": str(source.get("UF") or "").strip(),
        "CEP": str(source.get("CEP") or "").strip(),
    }
