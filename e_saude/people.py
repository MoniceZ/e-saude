from __future__ import annotations

import random
from dataclasses import dataclass
from datetime import date, datetime, timedelta

from faker import Faker


@dataclass(frozen=True)
class Parent:
    first_name: str
    surnames: list[str]
    birth_date: date


class PersonGenerator:
    """Gera os campos pessoais e familiares do dataset."""

    def __init__(
        self,
        locale: str = "pt_BR",
        seed: int | None = None,
        surname_pool_size: int = 50,
    ) -> None:
        self.fake = Faker([locale])
        self.random = random.Random(seed)
        if seed is not None:
            self.fake.seed_instance(seed)
        self.surnames = self._generate_surnames(surname_pool_size)

    def generate(self) -> dict[str, str]:
        gender = self._gender()
        father = self._parent("Masculino", min_age=17, max_age=50)
        mother = self._parent("Feminino", min_age=16, max_age=40)

        self.surnames.extend(father.surnames)
        self.surnames.extend(mother.surnames)

        child_birth_date = self._child_birth_date(father.birth_date, mother.birth_date)
        child_name, surname_1, surname_2 = self._child_name(father, mother, gender)
        child_age = self._age(child_birth_date)

        return {
            "Nome do Filho(a)": self._join_name(child_name, surname_1, surname_2),
            "Gênero": gender,
            "RG": self._rg(),
            "CPF": self._cpf(),
            "Data de Nascimento Filho(a)": self._format_date(child_birth_date),
            "Estado Civil": self._marital_status(child_age),
            "Pai": self._join_name(father.first_name, *father.surnames),
            "Data de Nascimento Pai": self._format_date(father.birth_date),
            "Mãe": self._join_name(mother.first_name, *mother.surnames),
            "Data de Nascimento Mãe": self._format_date(mother.birth_date),
        }

    def _generate_surnames(self, quantity: int) -> list[str]:
        surnames: set[str] = set()
        while len(surnames) < quantity:
            surnames.add(self.fake.last_name())
        return list(surnames)

    def _gender(self) -> str:
        return self.random.choices(["Masculino", "Feminino"], weights=[0.49, 0.51], k=1)[0]

    def _parent(self, gender: str, min_age: int, max_age: int) -> Parent:
        today = datetime.now().date()
        min_birth_date = today - timedelta(days=max_age * 365)
        max_birth_date = today - timedelta(days=min_age * 365)
        birth_date = self.fake.date_between_dates(
            date_start=min_birth_date,
            date_end=max_birth_date,
        )
        first_name = (
            self.fake.first_name_male()
            if gender == "Masculino"
            else self.fake.first_name_female()
        )
        surnames = self.random.sample(self.surnames, k=min(2, len(self.surnames)))
        return Parent(first_name=first_name, surnames=surnames, birth_date=birth_date)

    def _child_birth_date(self, father_birth_date: date, mother_birth_date: date) -> date:
        youngest_parent_birth_date = max(father_birth_date, mother_birth_date)
        min_birth_date = youngest_parent_birth_date + timedelta(days=16 * 365)
        max_birth_date = datetime.now().date()
        if min_birth_date > max_birth_date:
            min_birth_date = max_birth_date
        return self.fake.date_between_dates(
            date_start=min_birth_date,
            date_end=max_birth_date,
        )

    def _child_name(self, father: Parent, mother: Parent, gender: str) -> tuple[str, str, str]:
        first_name = (
            self.fake.first_name_male()
            if gender == "Masculino"
            else self.fake.first_name_female()
        )
        family_surnames = father.surnames + mother.surnames
        surname_1 = self.random.choice(family_surnames) if family_surnames else ""
        remaining = [surname for surname in family_surnames if surname != surname_1]
        surname_2 = self.random.choice(remaining) if remaining else ""
        return first_name, surname_1, surname_2

    def _rg(self) -> str:
        return str(self.fake.random_number(digits=7)).zfill(7)

    def _cpf(self) -> str:
        cpf = str(self.fake.random_number(digits=11)).zfill(11)
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    def _marital_status(self, age: int) -> str:
        if age < 18:
            return "Solteiro(a)"
        return self.random.choices(
            ["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"],
            weights=[42.8, 45.8, 6.0, 5.4],
            k=1,
        )[0]

    @staticmethod
    def _age(birth_date: date) -> int:
        return (datetime.now().date() - birth_date).days // 365

    @staticmethod
    def _format_date(value: date) -> str:
        return value.strftime("%d/%m/%Y")

    @staticmethod
    def _join_name(*parts: str) -> str:
        return " ".join(part for part in parts if part).strip()
