from __future__ import annotations

from collections.abc import Iterator

from .addresses import AddressProvider
from .config import GenerationConfig
from .people import PersonGenerator


def generate_records(config: GenerationConfig) -> Iterator[dict[str, str]]:
    person_generator = PersonGenerator(
        locale=config.locale,
        seed=config.seed,
        surname_pool_size=config.surname_pool_size,
    )
    address_provider = AddressProvider(
        path=config.addresses_path,
        seed=config.seed,
        delimiter=config.delimiter,
        encoding=config.encoding,
    )

    for _ in range(config.quantity):
        record = person_generator.generate()
        record.update(address_provider.get())
        yield record
