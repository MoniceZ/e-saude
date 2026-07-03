from __future__ import annotations

import csv
import random
import zipfile
from collections.abc import Iterator
from pathlib import Path
from typing import TextIO

from faker import Faker

from .schema import ADDRESS_FIELDS


EMPTY_ADDRESS = {field: "" for field in ADDRESS_FIELDS}


class AddressProvider:
    """Fornece endereços a partir de CSV comum ou CSV dentro de ZIP."""

    def __init__(
        self,
        path: Path | None = None,
        seed: int | None = None,
        delimiter: str = ";",
        encoding: str = "utf-8-sig",
    ) -> None:
        self.path = path
        self.delimiter = delimiter
        self.encoding = encoding
        self.random = random.Random(seed)
        self._addresses = list(self._load()) if path else []

    def get(self) -> dict[str, str]:
        if not self._addresses:
            return dict(EMPTY_ADDRESS)
        return dict(self.random.choice(self._addresses))

    def _load(self) -> Iterator[dict[str, str]]:
        if self.path is None:
            return

        suffix = self.path.suffix.lower()
        if suffix == ".zip":
            yield from self._load_zip(self.path)
        elif suffix == ".csv":
            with self.path.open("r", encoding=self.encoding, newline="") as file:
                yield from self._read_csv(file)
        else:
            raise ValueError(
                f"Formato de endereço não suportado: {self.path}. Use .csv ou .zip."
            )

    def _load_zip(self, path: Path) -> Iterator[dict[str, str]]:
        with zipfile.ZipFile(path) as archive:
            csv_names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            if not csv_names:
                raise ValueError(f"Nenhum CSV encontrado em {path}.")
            with archive.open(csv_names[0]) as file:
                lines = (line.decode(self.encoding, errors="replace") for line in file)
                yield from self._read_csv(lines)

    def _read_csv(self, rows: TextIO | Iterator[str]) -> Iterator[dict[str, str]]:
        reader = csv.DictReader(rows, delimiter=self.delimiter)
        for row in reader:
            yield {field: (row.get(field) or "") for field in ADDRESS_FIELDS}


class FakerAddressProvider:
    """Gera endereços sintéticos quando não houver base pública/cache."""

    def __init__(self, locale: str = "pt_BR", seed: int | None = None) -> None:
        self.fake = Faker([locale])
        self.random = random.Random(seed)
        if seed is not None:
            self.fake.seed_instance(seed)

    def get(self) -> dict[str, str]:
        return {
            "LOGRADOURO": self.fake.street_name(),
            "NUMERO": str(self.random.randint(1, 9999)),
            "COMPLEMENTO": self.random.choice(["N/A", "Casa", "Apto 101", "Bloco A"]),
            "BAIRRO": self.fake.bairro(),
            "MUNICIPIO": self.fake.city(),
            "UF": self.fake.estado_sigla(),
            "CEP": self.fake.postcode(),
        }
