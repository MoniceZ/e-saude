# E-Saúde - Gerador de Dados e Dataset

Projeto desenvolvido como Trabalho de Conclusão de Curso da Pós-graduação em Banco de Dados com Big Data, com o objetivo de estudar a geração de dados sintéticos para testes em sistemas de informação, especialmente no contexto da área da saúde.

A proposta principal deste projeto é gerar um conjunto de dados simulados contendo informações demográficas e cadastrais de pessoas/pacientes, possibilitando a realização de testes, validações e estudos sem a necessidade de utilizar dados reais ou sensíveis.

> Importante: este projeto foi desenvolvido exclusivamente para fins acadêmicos, educacionais e de estudo. Os dados gerados são sintéticos e não devem ser utilizados para representar pessoas reais.

## Objetivo do trabalho

O objetivo geral é desenvolver uma solução para geração e armazenamento de dados demográficos sintéticos para teste em sistemas de informação. Esta solução visa fornecer informações simuladas sobre pacientes, incluindo gênero, idade, endereço e outras características cadastrais.

A utilização de dados sintéticos permite testar aplicações, validar estruturas de banco de dados, simular cenários e realizar estudos sem expor informações reais de pacientes ou usuários.

Dessa forma, o projeto busca contribuir para o estudo de soluções que auxiliem no desenvolvimento e validação de sistemas, principalmente em contextos nos quais o uso de dados reais pode envolver questões de privacidade, segurança e conformidade com a legislação.

## Contexto acadêmico

A motivação do trabalho surgiu da necessidade de criar bases de dados para testes em sistemas de informação sem utilizar dados reais de pacientes. Em áreas como saúde, educação, gestão pública e sistemas corporativos, é comum que equipes de desenvolvimento precisem de dados para validar funcionalidades, relatórios, consultas, dashboards e integrações.

Entretanto, o uso de dados reais pode gerar riscos relacionados à privacidade e segurança da informação. Por isso, a geração de dados sintéticos se apresenta como uma alternativa viável para ambientes de desenvolvimento, testes e estudos acadêmicos.

## Funcionalidades

- Geração de dados sintéticos de pessoas.
- Criação de nomes completos simulados.
- Geração de documentos fictícios, como CPF e RG.
- Geração de informações familiares, como nome do pai e nome da mãe.
- Criação de informações demográficas, como idade, gênero e estado civil.
- Utilização opcional de dados públicos ou sintéticos para apoio na composição de endereços.
- Criação de dataset em estrutura tabular.
- Exportação dos dados em CSV.
- Possibilidade de uso do dataset gerado em testes, análises e estudos.
- Apoio a estudos relacionados a Banco de Dados, Big Data e sistemas de informação em saúde.

## Explicações por item/arquivo

- `main.py`: arquivo principal para iniciar a aplicação. Quando executado sem argumentos, abre a interface gráfica. Quando recebe argumentos, executa a interface de linha de comando.
- `e_saude/generator.py`: orquestra a geração dos registros sintéticos.
- `e_saude/people.py`: gera dados de pessoas, documentos fictícios e composição familiar.
- `e_saude/addresses.py`: realiza leitura e geração de endereços.
- `e_saude/elasticnes.py`: permite baixar e salvar um cache local de endereços públicos do ElastiCNES.
- `e_saude/exporters.py`: exporta o dataset final em CSV.
- `e_saude/gui.py`: interface gráfica desenvolvida com `customtkinter`.
- `e_saude/cli.py`: comandos disponíveis via terminal.
- `e_saude/schema.py`: define a ordem das colunas exportadas.
- `requirements.txt`: lista as bibliotecas necessárias para executar o projeto.
- `temp_dataframe.zip`: exemplo de dataset gerado, usado como referência da estrutura final dos dados.

## Tecnologias e conceitos utilizados

- Python
- Pandas e manipulação de dados, no contexto original do estudo
- Faker
- CustomTkinter
- Google Colab, como ambiente original de desenvolvimento
- Geração de dados sintéticos
- Criação de datasets
- Banco de Dados
- Big Data
- Dados públicos
- Sistemas de informação em saúde

## Instalação

Recomenda-se usar um ambiente virtual para instalar as dependências do projeto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Dependências principais:

- `Faker`
- `customtkinter`

## Como executar

Para abrir a interface gráfica:

```bash
python main.py
```

Na interface é possível:

- Definir a quantidade de registros.
- Escolher o arquivo de saída.
- Usar endereço vazio, endereço sintético com Faker ou arquivo CSV/ZIP/cache local.
- Informar uma seed para resultados reprodutíveis.
- Baixar cache de endereços públicos do ElastiCNES por limite, UF e competência.

Também é possível executar o projeto pela linha de comando.

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

Ver todas as opções disponíveis:

```bash
python main.py --help
```

## Endereços via ElastiCNES

O dataset de endereços utilizado no projeto pode ser obtido a partir da fonte pública:

```text
https://elasticnes.saude.gov.br
```

Como essa fonte possui limitações de disponibilidade, volume e acesso, a quantidade de dados retornados pode variar. Ainda assim, trata-se de uma base pública útil para fins acadêmicos, testes e simulações.

O projeto possui um comando para baixar endereços públicos do ElastiCNES e salvar um cache CSV local. A geração pode usar esse cache posteriormente, sem depender da internet a cada execução.

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
- A fonte pública pode mudar URL, formato de retorno ou disponibilidade.
- Os dados pessoais continuam sendo sintéticos. O ElastiCNES é usado apenas como apoio para campos públicos de endereço de estabelecimentos.

## Exemplo de dados gerados

O dataset gerado pode conter campos semelhantes aos listados abaixo:

| Campo | Descrição |
| --- | --- |
| Nome do Filho(a) | Nome completo gerado de forma sintética. |
| Gênero | Informação demográfica simulada. |
| RG | Número de RG fictício utilizado apenas para composição cadastral. |
| CPF | Número de CPF fictício utilizado apenas para testes. |
| Data de Nascimento Filho(a) | Data de nascimento simulada. |
| Estado Civil | Estado civil simulado para o cadastro da pessoa. |
| Pai | Nome gerado de forma sintética para composição familiar. |
| Data de Nascimento Pai | Data de nascimento simulada do pai. |
| Mãe | Nome gerado de forma sintética para composição familiar. |
| Data de Nascimento Mãe | Data de nascimento simulada da mãe. |
| LOGRADOURO, NUMERO, COMPLEMENTO, BAIRRO, MUNICIPIO, UF, CEP | Campos de endereço, quando uma fonte de endereços é informada. |

O arquivo `temp_dataframe.zip` contém um CSV de exemplo com a estrutura final esperada. O gerador consegue ler CSV diretamente ou um ZIP que contenha um CSV com as colunas de endereço:

```text
LOGRADOURO;NUMERO;COMPLEMENTO;BAIRRO;MUNICIPIO;UF;CEP
```

Se nenhum arquivo de endereços for informado, os campos de endereço continuam no CSV, mas ficam vazios. Isso preserva o schema final e facilita integrações.

## Possíveis aplicações

Embora o projeto tenha sido desenvolvido com finalidade acadêmica, ele pode servir como base de estudo para diferentes cenários, como:

- Testes de sistemas de informação.
- Validação de estruturas de banco de dados.
- Criação de bases simuladas para desenvolvimento.
- Estudos de modelagem de dados.
- Testes de relatórios e dashboards.
- Simulações em sistemas de saúde.
- Estudos com Python.
- Projetos acadêmicos envolvendo dados demográficos.
- Criação de datasets para ambientes de teste.

## Particularidades

O código foi desenvolvido originalmente no Google Colab. Por esse motivo, ao executá-lo em ambiente local, como VS Code, Jupyter Notebook ou terminal Python, podem ser necessários ajustes de ambiente, caminhos, arquivos e dependências.

A versão atual do projeto também possui uma estrutura Python modular, interface gráfica, linha de comando e comandos para geração ou download de endereços. Essas adaptações foram feitas para facilitar a execução local e tornar o projeto mais organizado.

Os dados gerados pelo projeto são sintéticos. Mesmo quando utilizados dados públicos para composição de endereços, as informações pessoais geradas, como nomes, documentos e vínculos familiares, não devem ser interpretadas como dados reais.

O projeto não foi desenvolvido com foco em ambiente produtivo. Seu objetivo é acadêmico, servindo como base para estudos de geração de dados, banco de dados, Big Data, sistemas de informação em saúde e manipulação de datasets com Python.

## Limitações

- O projeto foi desenvolvido para fins acadêmicos e de estudo.
- Não foi projetado para uso em ambiente de produção.
- Pode exigir ajustes conforme o ambiente local utilizado.
- A disponibilidade dos dados de endereço depende da fonte pública utilizada.
- Os dados gerados são sintéticos e não representam pessoas reais.
- Não há garantia de compatibilidade com todas as versões futuras das bibliotecas utilizadas.

## Privacidade e uso de dados

Este projeto tem como princípio evitar o uso de dados pessoais reais. As informações geradas são sintéticas e utilizadas apenas para compor uma base de testes.

Mesmo assim, recomenda-se cautela ao utilizar, adaptar ou expandir este projeto, especialmente em contextos que envolvam saúde, dados pessoais ou informações sensíveis.

Caso o projeto seja adaptado para ambientes reais, é necessário avaliar requisitos legais, técnicos e de segurança, incluindo normas de proteção de dados aplicáveis.

## Aviso sobre LGPD

Este projeto não utiliza dados pessoais reais gerados a partir de pacientes ou usuários identificáveis. O objetivo é justamente permitir estudos e testes utilizando dados sintéticos.

Ainda assim, qualquer adaptação que envolva dados reais deve observar a Lei Geral de Proteção de Dados Pessoais - LGPD e demais normas aplicáveis.

O uso deste projeto não substitui avaliações jurídicas, técnicas ou de segurança da informação em ambientes reais.

## Melhorias futuras

- Refatorar e ampliar a estrutura modular do projeto.
- Criar documentação técnica das funções.
- Adicionar testes automatizados.
- Permitir exportação em diferentes formatos, como JSON e Excel.
- Adicionar opção de geração de dados por estado, cidade ou região.
- Melhorar o tratamento de erros na coleta de dados públicos.
- Criar exemplos adicionais de uso.
- Expandir as opções de configuração da interface gráfica.

## Contribuições

Sinta-se livre para contribuir com comentários, códigos, lógicas, melhorias, correções e sugestões.

Algumas formas de contribuição incluem:

- Melhorias na organização do código.
- Correção de bugs.
- Refatoração das funções existentes.
- Melhoria na documentação.
- Criação de testes.
- Novas formas de geração de dados sintéticos.
- Melhorias na exportação dos datasets.
- Adaptação para execução fora do Google Colab.

## Licença

Este projeto pode ser utilizado para fins acadêmicos, educacionais e de estudo.

Recomenda-se utilizar uma licença aberta, como a MIT License, caso o objetivo seja permitir que outras pessoas usem, modifiquem e contribuam com o projeto.

Caso utilize a licença MIT, recomenda-se criar um arquivo separado chamado `LICENSE` na raiz do repositório contendo o texto completo da licença.

## Declaração de finalidade

Este repositório tem finalidade exclusivamente acadêmica e educacional. Ele foi desenvolvido como parte de um projeto de conclusão de curso e tem como objetivo demonstrar uma solução para geração de dados sintéticos voltados a testes de sistemas de informação.

O projeto não possui finalidade comercial, não deve ser utilizado como ferramenta oficial de geração de dados clínicos e não substitui soluções especializadas de anonimização, pseudonimização ou governança de dados.

## Autores

Criado por:

- Fábio Monice
- MONICE, F. J. C.
- Eliana Mendes

Orientado por:

- Professor Iwens Sene

## Observação final

Este projeto representa uma etapa de aprendizado e aplicação prática de conceitos relacionados a desenvolvimento, banco de dados, Big Data e geração de datasets sintéticos.

Melhorias, comentários e sugestões são bem-vindos.
