from __future__ import annotations

import csv
from collections.abc import Iterable
from pathlib import Path

from .schema import CSV_FIELDS


def write_csv(
    records: Iterable[dict[str, str]],
    output: Path,
    delimiter: str = ";",
    encoding: str = "utf-8-sig",
) -> int:
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0

    with output.open("w", newline="", encoding=encoding) as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS, delimiter=delimiter)
        writer.writeheader()
        for record in records:
            writer.writerow({field: record.get(field, "") for field in CSV_FIELDS})
            count += 1

    return count
