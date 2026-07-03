from __future__ import annotations

import argparse
from pathlib import Path

from .config import GenerationConfig
from .elasticnes import ElasticnesError, download_elasticnes_addresses


DEFAULT_CACHE_PATH = Path("data/enderecos_elasticnes.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gera dados sintéticos de pacientes para estudos e testes."
    )
    subparsers = parser.add_subparsers(dest="command")

    download_parser = subparsers.add_parser(
        "baixar-enderecos",
        help="Baixa endereços públicos do ElastiCNES para um cache CSV local.",
    )
    download_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_CACHE_PATH,
        help=f"Arquivo CSV de cache. Padrão: {DEFAULT_CACHE_PATH}.",
    )
    download_parser.add_argument(
        "--limit",
        type=int,
        default=1_000,
        help="Quantidade máxima de endereços a baixar. Padrão: 1000.",
    )
    download_parser.add_argument("--uf", default=None, help="Filtra por UF, exemplo: SP.")
    download_parser.add_argument(
        "--competencia",
        default="202605",
        help="Competência do ElastiCNES no formato aaaamm. Padrão: 202605.",
    )
    download_parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Timeout da consulta em segundos. Padrão: 30.",
    )

    _add_generation_arguments(parser)
    return parser


def _add_generation_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "-q",
        "--quantity",
        type=int,
        default=1_000,
        help="Quantidade de registros a gerar. Padrão: 1000.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("registros.csv"),
        help="Arquivo CSV de saída. Padrão: registros.csv.",
    )
    parser.add_argument(
        "-a",
        "--addresses",
        type=Path,
        default=None,
        help="CSV ou ZIP com endereços. Se informado, tem prioridade sobre --address-source.",
    )
    parser.add_argument(
        "--address-source",
        choices=["none", "faker"],
        default="none",
        help="Fonte alternativa de endereço quando --addresses não for informado.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Semente para resultados reprodutíveis.",
    )


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "baixar-enderecos":
        return _download_addresses(args)
    return _generate(args)


def _download_addresses(args: argparse.Namespace) -> int:
    if args.limit < 1:
        raise SystemExit("O limite deve ser maior que zero.")

    try:
        count = download_elasticnes_addresses(
            output=args.output,
            limit=args.limit,
            uf=args.uf,
            competencia=args.competencia,
            timeout=args.timeout,
        )
    except ElasticnesError as error:
        raise SystemExit(str(error)) from error

    print(f"{count} endereços foram baixados para {args.output}.")
    return 0


def _generate(args: argparse.Namespace) -> int:
    from .exporters import write_csv
    from .generator import generate_records

    if args.quantity < 1:
        raise SystemExit("A quantidade deve ser maior que zero.")

    config = GenerationConfig(
        quantity=args.quantity,
        output=args.output,
        addresses_path=args.addresses,
        address_source=args.address_source,
        seed=args.seed,
    )
    count = write_csv(generate_records(config), config.output, config.delimiter, config.encoding)
    print(f"{count} registros foram gerados e exportados para {config.output}.")
    return 0
