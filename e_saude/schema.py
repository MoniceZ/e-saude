"""Campos exportados pelo dataset."""

PERSON_FIELDS = [
    "Nome do Filho(a)",
    "Gênero",
    "RG",
    "CPF",
    "Data de Nascimento Filho(a)",
    "Estado Civil",
    "Pai",
    "Data de Nascimento Pai",
    "Mãe",
    "Data de Nascimento Mãe",
]

ADDRESS_FIELDS = [
    "LOGRADOURO",
    "NUMERO",
    "COMPLEMENTO",
    "BAIRRO",
    "MUNICIPIO",
    "UF",
    "CEP",
]

CSV_FIELDS = PERSON_FIELDS + ADDRESS_FIELDS
