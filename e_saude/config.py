from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GenerationConfig:
    """Parâmetros principais para geração do dataset."""

    quantity: int = 1_000
    output: Path = Path("registros.csv")
    addresses_path: Path | None = None
    address_source: str = "none"
    seed: int | None = None
    delimiter: str = ";"
    encoding: str = "utf-8-sig"
    locale: str = "pt_BR"
    surname_pool_size: int = 50
