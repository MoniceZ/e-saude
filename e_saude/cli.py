from __future__ import annotations

import argparse
from pathlib import Path

from .config import GenerationConfig
from .exporters import write_csv
from .generator import generate_records


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gera dados sinteticos de pacientes para estudos e testes."
    )
    parser.add_argument(
        "-q",
        "--quantity",
        type=int,
        default=1_000,
        help="Quantidade de registros a gerar. Padrao: 1000.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("registros.csv"),
        help="Arquivo CSV de saida. Padrao: registros.csv.",
    )
    parser.add_argument(
        "-a",
        "--addresses",
        type=Path,
        default=None,
        help="CSV ou ZIP com enderecos no schema do temp_dataframe.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Semente para resultados reprodutiveis.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.quantity < 1:
        raise SystemExit("A quantidade deve ser maior que zero.")

    config = GenerationConfig(
        quantity=args.quantity,
        output=args.output,
        addresses_path=args.addresses,
        seed=args.seed,
    )
    count = write_csv(generate_records(config), config.output, config.delimiter, config.encoding)
    print(f"{count} registros foram gerados e exportados para {config.output}.")
    return 0
