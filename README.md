# E-Saude - Gerador de Dados Sinteticos

Projeto academico para gerar datasets sinteticos de pessoas/pacientes, com dados cadastrais, familiares, documentos ficticios e enderecos opcionais. A proposta e apoiar testes, validacoes, estudos de banco de dados e simulacoes sem expor dados pessoais reais.

> Importante: todos os dados pessoais gerados sao sinteticos e devem ser usados apenas para fins educacionais, testes e estudos.

## O que o projeto gera

O CSV final segue o schema observado no `temp_dataframe.zip`:

| Campo | Descricao |
| --- | --- |
| Nome do Filho(a) | Nome completo sintetico |
| Genero | Masculino ou Feminino |
| RG | Documento ficticio com 7 digitos |
| CPF | CPF ficticio formatado |
| Data de Nascimento Filho(a) | Data no formato `dd/mm/aaaa` |
| Estado Civil | Estado civil simulado conforme idade |
| Pai | Nome sintetico do pai |
| Data de Nascimento Pai | Data no formato `dd/mm/aaaa` |
| Mae | Nome sintetico da mae |
| Data de Nascimento Mae | Data no formato `dd/mm/aaaa` |
| LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO, UF, CEP | Campos de endereco, quando uma base de enderecos e informada |

## Estrutura

```text
e_saude/
  addresses.py    # Leitura de enderecos de CSV ou ZIP
  cli.py          # Interface de linha de comando
  config.py       # Configuracoes da geracao
  exporters.py    # Escrita do CSV
  generator.py    # Orquestracao dos registros
  people.py       # Geracao de pessoas, documentos e familia
  schema.py       # Ordem oficial das colunas
gerador_de_dados.py  # Entrada legada compatível com o projeto antigo
requirements.txt
requerimentos.txt
pyproject.toml
```

## Instalação

Recomenda-se usar ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

O arquivo `requerimentos.txt` foi mantido por compatibilidade, mas agora tambem contem apenas dependencias instalaveis pelo `pip`.

## Como executar

Gerar 1.000 registros sem enderecos:

```bash
python gerador_de_dados.py
```

Gerar uma quantidade especifica:

```bash
python gerador_de_dados.py --quantity 10000 --output output/registros.csv
```

Usar o ZIP de exemplo como fonte de enderecos:

```bash
python gerador_de_dados.py --quantity 1000 --addresses temp_dataframe.zip --output output/registros_com_endereco.csv
```

Gerar resultado reprodutivel com seed:

```bash
python gerador_de_dados.py --quantity 100 --seed 42
```

Ver todas as opcoes:

```bash
python gerador_de_dados.py --help
```

## Dataset de exemplo

O arquivo `temp_dataframe.zip` contem um CSV de exemplo (`temp_dataframe.csv`) com a estrutura final esperada. O gerador consegue ler CSV diretamente ou um ZIP que contenha um CSV com as colunas de endereco:

```text
LOGRADOURO;NUMERO;COMPLEMENTO;BAIRRO;MUNICIPIO;UF;CEP
```

Se nenhum arquivo de enderecos for informado, os campos de endereco continuam no CSV, mas ficam vazios. Isso preserva o schema final e facilita integracoes.

## Principais melhorias da organizacao

- Separacao do codigo em modulos pequenos e reutilizaveis.
- CLI com argumentos para quantidade, saida, enderecos e seed.
- Escrita em streaming, sem guardar todos os registros em memoria.
- `requirements.txt` valido para instalacao local.
- `pyproject.toml` com metadados do pacote e comando `e-saude` para instalacao futura.
- `.gitignore` para evitar versionar ambientes virtuais, caches e CSVs gerados.

## Privacidade e LGPD

Este projeto nao utiliza dados pessoais reais para nomes, documentos ou vinculos familiares. Ainda assim, qualquer adaptacao com dados reais deve observar a LGPD e boas praticas de seguranca, governanca e protecao de dados.

## Contexto academico

Projeto desenvolvido como Trabalho de Conclusao de Curso da Pos-graduacao em Banco de Dados com Big Data, com foco no estudo de geracao de dados sinteticos para sistemas de informacao, especialmente no contexto da saude.

## Autores

Criado por Fabio Monice e Eliana Mendes. Orientacao: Professor Iwens Sene.
