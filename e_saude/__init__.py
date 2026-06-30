"""Gerador de dados sinteticos para estudos em sistemas de saude."""

from .config import GenerationConfig
from .generator import generate_records

__all__ = ["GenerationConfig", "generate_records"]
