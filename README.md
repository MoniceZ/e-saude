# E-Saúde - Gerador de Dados Sintéticos

Projeto acadêmico para gerar datasets sintéticos de pessoas/pacientes, com dados cadastrais, familiares, documentos fictícios e endereços opcionais. A proposta é apoiar testes, validações, estudos de banco de dados e simulações sem expor dados pessoais reais.

> Importante: todos os dados pessoais gerados são sintéticos e devem ser usados apenas para fins educacionais, testes e estudos.

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
| LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO, UF, CEP | Campos de endereço, quando uma base de endereços é informada |

## Estrutura

```text
e_saude/
  addresses.py    # Leitura de endereços de CSV ou ZIP
  cli.py          # Interface de linha de comando
  config.py       # Configurações da geração
  exporters.py    # Escrita do CSV
  generator.py    # Orquestração dos registros
  people.py       # Geração de pessoas, documentos e família
  schema.py       # Ordem oficial das colunas
main.py            # Entrada principal da aplicação
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

O arquivo `requerimentos.txt` foi mantido por compatibilidade, mas agora também contém apenas dependências instaláveis pelo `pip`.

## Como executar

Gerar 1.000 registros sem endereços:

```bash
python main.py
```

Gerar uma quantidade específica:

```bash
python main.py --quantity 10000 --output output/registros.csv
```

Usar o ZIP de exemplo como fonte de endereços:

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

## Dataset de exemplo

O arquivo `temp_dataframe.zip` contém um CSV de exemplo (`temp_dataframe.csv`) com a estrutura final esperada. O gerador consegue ler CSV diretamente ou um ZIP que contenha um CSV com as colunas de endereço:

```text
LOGRADOURO;NUMERO;COMPLEMENTO;BAIRRO;MUNICIPIO;UF;CEP
```

Se nenhum arquivo de endereços for informado, os campos de endereço continuam no CSV, mas ficam vazios. Isso preserva o schema final e facilita integrações.

## Principais melhorias da organização

- Separação do código em módulos pequenos e reutilizáveis.
- CLI com argumentos para quantidade, saída, endereços e seed.
- Escrita em streaming, sem guardar todos os registros em memória.
- `requirements.txt` válido para instalação local.
- `pyproject.toml` com metadados do pacote e comando `e-saude` para instalação futura.
- `.gitignore` para evitar versionar ambientes virtuais, caches e CSVs gerados.

## Privacidade e LGPD

Este projeto não utiliza dados pessoais reais para nomes, documentos ou vínculos familiares. Ainda assim, qualquer adaptação com dados reais deve observar a LGPD e boas práticas de segurança, governança e proteção de dados.

## Contexto acadêmico

Projeto desenvolvido como Trabalho de Conclusão de Curso da Pós-graduação em Banco de Dados com Big Data, com foco no estudo de geração de dados sintéticos para sistemas de informação, especialmente no contexto da saúde.

## Autores

Criado por Fábio Monice e Eliana Mendes. Orientação: Professor Iwens Sene.
