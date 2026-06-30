# E-Saúde - Gerador de Dados Sintéticos

Projeto acadêmico para gerar datasets sintéticos de pessoas/pacientes, com dados cadastrais, familiares, documentos fictícios e endereços opcionais. A proposta é apoiar testes, validações, estudos de banco de dados e simulações sem expor dados pessoais reais.

> Importante: todos os dados pessoais gerados são sintéticos e devem ser usados apenas para fins educacionais, testes e estudos.

## Interface gráfica

A aplicação possui uma interface em `customtkinter` para escolher os mesmos parâmetros disponíveis na linha de comando.

```bash
python main.py
```

Na interface é possível:

- Definir quantidade de registros.
- Escolher arquivo de saída.
- Usar endereço vazio, endereço sintético com Faker ou CSV/ZIP/cache local.
- Informar seed para resultados reprodutíveis.
- Baixar cache de endereços públicos do ElastiCNES por limite, UF e competência.

## O que o projeto gera

O CSV final segue o schema observado no `temp_dataframe.zip`:

| Campo | Descrição |
| --- | --- |
| Nome do Filho(a) | Nome completo sintético |
| Gênero | Masculino ou Feminino |
| RG | Documento fictício com 7 dígitos |
| CPF | CPF fictício formatado |
| Data de Nascimento Filho(a) | Data no formato `dd/mm/aaaa` |
| Estado Civil | Estado civil simulado conforme idade |
| Pai | Nome sintético do pai |
| Data de Nascimento Pai | Data no formato `dd/mm/aaaa` |
| Mãe | Nome sintético da mãe |
| Data de Nascimento Mãe | Data no formato `dd/mm/aaaa` |
| LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO, UF, CEP | Campos de endereço, quando uma fonte de endereços é informada |

## Estrutura

```text
e_saude/
  addresses.py    # Leitura e geração de endereços
  cli.py          # Interface de linha de comando
  config.py       # Configurações da geração
  elasticnes.py   # Download/cache de endereços públicos do ElastiCNES
  exporters.py    # Escrita do CSV
  generator.py    # Orquestração dos registros
  gui.py          # Interface gráfica customtkinter
  people.py       # Geração de pessoas, documentos e família
  schema.py       # Ordem oficial das colunas
main.py            # Entrada principal da aplicação
requirements.txt
pyproject.toml
```

## Instalação

Recomenda-se usar ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Linha de comando

A CLI continua disponível quando `main.py` recebe argumentos.

Gerar uma quantidade específica:

```bash
python main.py --quantity 10000 --output output/registros.csv
```

Gerar endereços sintéticos com Faker:

```bash
python main.py --quantity 1000 --address-source faker --output output/registros_com_endereco.csv
```

Usar um CSV ou ZIP local como fonte de endereços:

```bash
python main.py --quantity 1000 --addresses temp_dataframe.zip --output output/registros_com_endereco.csv
```

Gerar resultado reprodutível com seed:

```bash
python main.py --quantity 100 --seed 42
```

Ver todas as opções:

```bash
python main.py --help
```

## Endereços via ElastiCNES

O projeto possui um comando para baixar endereços públicos do ElastiCNES (`https://elasticnes.saude.gov.br/`) e salvar um cache CSV local. A geração usa esse cache depois, sem depender da internet a cada execução.

Baixar uma amostra padrão:

```bash
python main.py baixar-enderecos --limit 1000
```

Baixar por UF:

```bash
python main.py baixar-enderecos --uf SP --limit 10000 --output data/enderecos_elasticnes.csv
```

Gerar dados usando o cache baixado:

```bash
python main.py --quantity 1000 --addresses data/enderecos_elasticnes.csv --output output/registros.csv
```

Observações:

- O cache é ignorado pelo Git para evitar versionar dados baixados.
- A fonte pública pode mudar URL, payload ou disponibilidade; por isso o cache local é o caminho mais estável.
- Os dados pessoais continuam sendo sintéticos. O ElastiCNES é usado apenas como apoio para campos públicos de endereço de estabelecimentos.

## Dataset de exemplo

O arquivo `temp_dataframe.zip` contém um CSV de exemplo (`temp_dataframe.csv`) com a estrutura final esperada. O gerador consegue ler CSV diretamente ou um ZIP que contenha um CSV com as colunas de endereço:

```text
LOGRADOURO;NUMERO;COMPLEMENTO;BAIRRO;MUNICIPIO;UF;CEP
```

Se nenhum arquivo de endereços for informado, os campos de endereço continuam no CSV, mas ficam vazios. Isso preserva o schema final e facilita integrações.

## Privacidade e LGPD

Este projeto não utiliza dados pessoais reais para nomes, documentos ou vínculos familiares. Ainda assim, qualquer adaptação com dados reais deve observar a LGPD e boas práticas de segurança, governança e proteção de dados.

## Contexto acadêmico

Projeto desenvolvido como Trabalho de Conclusão de Curso da Pós-graduação em Banco de Dados com Big Data, com foco no estudo de geração de dados sintéticos para sistemas de informação, especialmente no contexto da saúde.

## Autores

Criado por Fábio Monice e Eliana Mendes. Orientação: Professor Iwens Sene.
