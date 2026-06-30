from __future__ import annotations

import threading
from pathlib import Path
from tkinter import filedialog

import customtkinter as ctk

from .config import GenerationConfig
from .elasticnes import ElasticnesError, download_elasticnes_addresses
from .exporters import write_csv
from .generator import generate_records


class ESudeApp(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("E-Saúde | Gerador de Dados Sintéticos")
        self.geometry("1080x720")
        self.minsize(980, 640)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self._build_state()
        self._build_layout()

    def _build_state(self) -> None:
        self.quantity_var = ctk.StringVar(value="1000")
        self.output_var = ctk.StringVar(value="output/registros.csv")
        self.address_source_var = ctk.StringVar(value="none")
        self.addresses_var = ctk.StringVar(value="")
        self.seed_var = ctk.StringVar(value="")

        self.download_limit_var = ctk.StringVar(value="1000")
        self.download_uf_var = ctk.StringVar(value="")
        self.download_competencia_var = ctk.StringVar(value="202605")
        self.download_timeout_var = ctk.StringVar(value="30")
        self.download_output_var = ctk.StringVar(value="data/enderecos_elasticnes.csv")

    def _build_layout(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header = ctk.CTkFrame(self, corner_radius=0, fg_color=("#f8fafc", "#111827"))
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text="E-Saúde",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        title.grid(row=0, column=0, padx=28, pady=(22, 2), sticky="w")

        subtitle = ctk.CTkLabel(
            header,
            text="Geração de datasets sintéticos com parâmetros configuráveis",
            text_color=("#475569", "#cbd5e1"),
            font=ctk.CTkFont(size=14),
        )
        subtitle.grid(row=1, column=0, padx=28, pady=(0, 20), sticky="w")

        self.tabs = ctk.CTkTabview(self, corner_radius=14)
        self.tabs.grid(row=1, column=0, padx=24, pady=24, sticky="nsew")
        self.tabs.add("Gerar dataset")
        self.tabs.add("ElastiCNES")

        self._build_generate_tab(self.tabs.tab("Gerar dataset"))
        self._build_download_tab(self.tabs.tab("ElastiCNES"))

    def _build_generate_tab(self, tab: ctk.CTkFrame) -> None:
        tab.grid_columnconfigure((0, 1), weight=1, uniform="generate")
        tab.grid_rowconfigure(0, weight=1)

        form = self._card(tab)
        form.grid(row=0, column=0, padx=(18, 9), pady=18, sticky="nsew")
        form.grid_columnconfigure(1, weight=1)

        self._section_title(form, "Parâmetros de geração", 0)
        self._entry(form, "Quantidade", self.quantity_var, 1)
        self._entry(form, "Arquivo de saída", self.output_var, 2, browse=self._choose_output_file)

        ctk.CTkLabel(form, text="Fonte de endereço").grid(row=3, column=0, padx=18, pady=12, sticky="w")
        source = ctk.CTkSegmentedButton(
            form,
            values=["none", "faker"],
            variable=self.address_source_var,
        )
        source.grid(row=3, column=1, padx=18, pady=12, sticky="ew")

        self._entry(form, "CSV/ZIP de endereços", self.addresses_var, 4, browse=self._choose_address_file)
        self._entry(form, "Seed", self.seed_var, 5)

        generate_button = ctk.CTkButton(
            form,
            text="Gerar CSV",
            height=44,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self._generate_dataset,
        )
        generate_button.grid(row=6, column=0, columnspan=2, padx=18, pady=(22, 18), sticky="ew")

        status = self._card(tab)
        status.grid(row=0, column=1, padx=(9, 18), pady=18, sticky="nsew")
        status.grid_rowconfigure(2, weight=1)
        status.grid_columnconfigure(0, weight=1)

        self._section_title(status, "Acompanhamento", 0)
        self.generate_progress = ctk.CTkProgressBar(status, mode="indeterminate")
        self.generate_progress.grid(row=1, column=0, padx=18, pady=(8, 16), sticky="ew")
        self.generate_log = ctk.CTkTextbox(status, corner_radius=10)
        self.generate_log.grid(row=2, column=0, padx=18, pady=(0, 18), sticky="nsew")
        self._log(self.generate_log, "Pronto para gerar o dataset.")

    def _build_download_tab(self, tab: ctk.CTkFrame) -> None:
        tab.grid_columnconfigure((0, 1), weight=1, uniform="download")
        tab.grid_rowconfigure(0, weight=1)

        form = self._card(tab)
        form.grid(row=0, column=0, padx=(18, 9), pady=18, sticky="nsew")
        form.grid_columnconfigure(1, weight=1)

        self._section_title(form, "Cache de endereços públicos", 0)
        self._entry(form, "Limite", self.download_limit_var, 1)
        self._entry(form, "UF", self.download_uf_var, 2)
        self._entry(form, "Competência", self.download_competencia_var, 3)
        self._entry(form, "Timeout", self.download_timeout_var, 4)
        self._entry(form, "Arquivo de cache", self.download_output_var, 5, browse=self._choose_cache_file)

        download_button = ctk.CTkButton(
            form,
            text="Baixar endereços",
            height=44,
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self._download_addresses,
        )
        download_button.grid(row=6, column=0, columnspan=2, padx=18, pady=(22, 18), sticky="ew")

        status = self._card(tab)
        status.grid(row=0, column=1, padx=(9, 18), pady=18, sticky="nsew")
        status.grid_rowconfigure(2, weight=1)
        status.grid_columnconfigure(0, weight=1)

        self._section_title(status, "Status do ElastiCNES", 0)
        self.download_progress = ctk.CTkProgressBar(status, mode="indeterminate")
        self.download_progress.grid(row=1, column=0, padx=18, pady=(8, 16), sticky="ew")
        self.download_log = ctk.CTkTextbox(status, corner_radius=10)
        self.download_log.grid(row=2, column=0, padx=18, pady=(0, 18), sticky="nsew")
        self._log(self.download_log, "Baixe um cache local antes de usar endereços do ElastiCNES.")

    def _card(self, parent: ctk.CTkFrame) -> ctk.CTkFrame:
        return ctk.CTkFrame(parent, corner_radius=16, border_width=1)

    def _section_title(self, parent: ctk.CTkFrame, text: str, row: int) -> None:
        label = ctk.CTkLabel(parent, text=text, font=ctk.CTkFont(size=18, weight="bold"))
        label.grid(row=row, column=0, columnspan=2, padx=18, pady=(18, 12), sticky="w")

    def _entry(
        self,
        parent: ctk.CTkFrame,
        label: str,
        variable: ctk.StringVar,
        row: int,
        browse=None,
    ) -> None:
        ctk.CTkLabel(parent, text=label).grid(row=row, column=0, padx=18, pady=12, sticky="w")
        entry = ctk.CTkEntry(parent, textvariable=variable, height=38)
        entry.grid(row=row, column=1, padx=(18, 8 if browse else 18), pady=12, sticky="ew")
        if browse:
            button = ctk.CTkButton(parent, text="...", width=44, height=38, command=browse)
            button.grid(row=row, column=2, padx=(0, 18), pady=12, sticky="e")

    def _choose_output_file(self) -> None:
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )
        if path:
            self.output_var.set(path)

    def _choose_address_file(self) -> None:
        path = filedialog.askopenfilename(
            filetypes=[("CSV ou ZIP", "*.csv *.zip"), ("Todos os arquivos", "*.*")],
        )
        if path:
            self.addresses_var.set(path)

    def _choose_cache_file(self) -> None:
        path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        )
        if path:
            self.download_output_var.set(path)

    def _generate_dataset(self) -> None:
        def task() -> None:
            self._start(self.generate_progress)
            try:
                quantity = self._positive_int(self.quantity_var.get(), "Quantidade")
                seed = self._optional_int(self.seed_var.get(), "Seed")
                addresses = self.addresses_var.get().strip()
                config = GenerationConfig(
                    quantity=quantity,
                    output=Path(self.output_var.get().strip()),
                    addresses_path=Path(addresses) if addresses else None,
                    address_source=self.address_source_var.get(),
                    seed=seed,
                )
                count = write_csv(generate_records(config), config.output, config.delimiter, config.encoding)
                self._log(self.generate_log, f"{count} registros gerados em {config.output}.")
            except Exception as error:
                self._log(self.generate_log, f"Erro: {error}")
            finally:
                self._stop(self.generate_progress)

        threading.Thread(target=task, daemon=True).start()

    def _download_addresses(self) -> None:
        def task() -> None:
            self._start(self.download_progress)
            try:
                count = download_elasticnes_addresses(
                    output=Path(self.download_output_var.get().strip()),
                    limit=self._positive_int(self.download_limit_var.get(), "Limite"),
                    uf=self.download_uf_var.get().strip() or None,
                    competencia=self.download_competencia_var.get().strip() or None,
                    timeout=self._positive_int(self.download_timeout_var.get(), "Timeout"),
                )
                self._log(self.download_log, f"{count} endereços baixados em {self.download_output_var.get()}.")
            except ElasticnesError as error:
                self._log(self.download_log, f"ElastiCNES: {error}")
            except Exception as error:
                self._log(self.download_log, f"Erro: {error}")
            finally:
                self._stop(self.download_progress)

        threading.Thread(target=task, daemon=True).start()

    def _start(self, progress: ctk.CTkProgressBar) -> None:
        self.after(0, progress.start)

    def _stop(self, progress: ctk.CTkProgressBar) -> None:
        self.after(0, progress.stop)

    def _log(self, textbox: ctk.CTkTextbox, message: str) -> None:
        def append() -> None:
            textbox.configure(state="normal")
            textbox.insert("end", f"{message}\n")
            textbox.see("end")
            textbox.configure(state="disabled")

        self.after(0, append)

    @staticmethod
    def _positive_int(value: str, field: str) -> int:
        try:
            parsed = int(value)
        except ValueError as error:
            raise ValueError(f"{field} deve ser um número inteiro.") from error
        if parsed < 1:
            raise ValueError(f"{field} deve ser maior que zero.")
        return parsed

    @staticmethod
    def _optional_int(value: str, field: str) -> int | None:
        if not value.strip():
            return None
        try:
            return int(value)
        except ValueError as error:
            raise ValueError(f"{field} deve ser um número inteiro.") from error


def run() -> None:
    app = ESudeApp()
    app.mainloop()
