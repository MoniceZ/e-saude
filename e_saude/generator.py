from __future__ import annotations

from collections.abc import Iterator

from .addresses import AddressProvider, FakerAddressProvider
from .config import GenerationConfig
from .people import PersonGenerator


def generate_records(config: GenerationConfig) -> Iterator[dict[str, str]]:
    person_generator = PersonGenerator(
        locale=config.locale,
        seed=config.seed,
        surname_pool_size=config.surname_pool_size,
    )
    address_provider = _build_address_provider(config)

    for _ in range(config.quantity):
        record = person_generator.generate()
        record.update(address_provider.get())
        yield record


def _build_address_provider(config: GenerationConfig):
    if config.addresses_path:
        return AddressProvider(
            path=config.addresses_path,
            seed=config.seed,
            delimiter=config.delimiter,
            encoding=config.encoding,
        )
    if config.address_source == "faker":
        return FakerAddressProvider(locale=config.locale, seed=config.seed)
    return AddressProvider(seed=config.seed)
