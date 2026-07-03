"""Entrada principal da aplicação."""

from __future__ import annotations

import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        from e_saude.gui import run

        run()
    else:
        from e_saude.cli import main

        raise SystemExit(main())
