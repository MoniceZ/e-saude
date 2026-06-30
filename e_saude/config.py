from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class GenerationConfig:
    """Parametros principais para geracao do dataset."""

    quantity: int = 1_000
    output: Path = Path("registros.csv")
    addresses_path: Path | None = None
    seed: int | None = None
    delimiter: str = ";"
    encoding: str = "utf-8-sig"
    locale: str = "pt_BR"
    surname_pool_size: int = 50
