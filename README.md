# E-Saúde - Gerador de Dados e Dataset

<p>
  Projeto desenvolvido como Trabalho de Conclusão de Curso da Pós-graduação em <strong>Banco de Dados com Big Data</strong>, com o objetivo de estudar a geração de dados sintéticos para testes em sistemas de informação, especialmente no contexto da área da saúde.
</p>

<p>
  A proposta principal deste projeto é gerar um conjunto de dados simulados contendo informações demográficas e cadastrais de pessoas/pacientes, possibilitando a realização de testes, validações e estudos sem a necessidade de utilizar dados reais ou sensíveis.
</p>

<p>
  <strong>Importante:</strong> este projeto foi desenvolvido exclusivamente para fins acadêmicos, educacionais e de estudo. Os dados gerados são sintéticos e não devem ser utilizados para representar pessoas reais.
</p>

---

## Explicações por item/arquivo:

<ol> 
  <li>
    <img src="https://user-images.githubusercontent.com/113941301/255664814-a85bc430-2cb8-4014-a835-eb40367ea459.png" width="15" />
    <strong> gerador_de_dados:</strong> 
    arquivo principal do projeto, responsável pela geração dos dados sintéticos de pessoas. Ele cria informações como nomes, CPFs, RGs, estado civil, nome do pai, nome da mãe, gênero, idade, endereço e demais dados cadastrais utilizados na composição do dataset.
  </li>

  <br />

  <li>
    <img src="https://user-images.githubusercontent.com/113941301/255906581-b1634c21-222b-4cc5-8378-4516ae15c785.png" width="15" />
    <strong> requerimentos:</strong> 
    arquivo contendo a lista de bibliotecas e dependências utilizadas no projeto. Ele serve como referência para instalação dos pacotes necessários para executar o código corretamente.
  </li>

  <br />

  <li>
    <img src="https://user-images.githubusercontent.com/113941301/255664380-3e5d435e-7581-4fbf-923c-2ea451151036.png" width="15" />
    <strong> temp_dataframe:</strong> 
    exemplo de dataset gerado a partir deste projeto. Esse arquivo demonstra a estrutura final dos dados produzidos, permitindo visualizar o resultado da geração antes de realizar novas execuções ou adaptações.
  </li>
</ol>

---

## Explicações de Particularidades

<ol>
  <li>
    <p>
      O código foi desenvolvido originalmente no <strong>Google Colab</strong>. Por esse motivo, ao tentar executá-lo em um ambiente local, como VS Code, Jupyter Notebook ou terminal Python, pode ser necessário reorganizar caminhos, arquivos, imports e dependências.
    </p>
  </li>

  <li>
    <p>
      O dataset de endereços utilizado no projeto é obtido a partir da fonte pública:
      <br />
      <a href="https://elasticnes.saude.gov.br">https://elasticnes.saude.gov.br</a>
    </p>
    <p>
      Como essa fonte possui limitações de disponibilidade, volume e acesso, a quantidade de dados retornados pode variar. Ainda assim, trata-se de uma base pública útil para fins acadêmicos, testes e simulações.
    </p>
  </li>

  <li>
    <p>
      Os dados gerados pelo projeto são sintéticos. Mesmo quando utilizados dados públicos para composição de endereços, as informações pessoais geradas, como nomes, documentos e vínculos familiares, não devem ser interpretadas como dados reais.
    </p>
  </li>

  <li>
    <p>
      O projeto não foi desenvolvido com foco em ambiente produtivo. Seu objetivo é acadêmico, servindo como base para estudos de geração de dados, banco de dados, Big Data, sistemas de informação em saúde e manipulação de datasets com Python.
    </p>
  </li>
</ol>

---

## Objetivo desse trabalho

<p>
  O objetivo geral é desenvolver uma solução para a geração e/ou armazenamento de dados demográficos sintéticos para teste em sistemas de informação. Esta solução visa fornecer informações simuladas sobre pacientes, incluindo gênero, idade, endereço e outras características cadastrais.
</p>

<p>
  A utilização de dados sintéticos permite testar aplicações, validar estruturas de banco de dados, simular cenários e realizar estudos sem expor informações reais de pacientes ou usuários.
</p>

<p>
  Dessa forma, o projeto busca contribuir para o estudo de soluções que auxiliem no desenvolvimento e validação de sistemas, principalmente em contextos nos quais o uso de dados reais pode envolver questões de privacidade, segurança e conformidade com a legislação.
</p>

---

## Contexto Acadêmico

<p>
  Este projeto foi desenvolvido como parte de um Trabalho de Conclusão de Curso da Pós-graduação em <strong>Banco de Dados com Big Data</strong>.
</p>

<p>
  A motivação do trabalho surgiu da necessidade de criar bases de dados para testes em sistemas de informação sem utilizar dados reais de pacientes. Em áreas como saúde, educação, gestão pública e sistemas corporativos, é comum que equipes de desenvolvimento precisem de dados para validar funcionalidades, relatórios, consultas, dashboards e integrações.
</p>

<p>
  Entretanto, o uso de dados reais pode gerar riscos relacionados à privacidade e segurança da informação. Por isso, a geração de dados sintéticos se apresenta como uma alternativa viável para ambientes de desenvolvimento, testes e estudos acadêmicos.
</p>

---

## Funcionalidades

<ol>
  <li>Geração de dados sintéticos de pessoas.</li>
  <li>Criação de nomes completos simulados.</li>
  <li>Geração de documentos fictícios, como CPF e RG.</li>
  <li>Geração de informações familiares, como nome do pai e nome da mãe.</li>
  <li>Criação de informações demográficas, como idade, gênero e estado civil.</li>
  <li>Utilização de dados públicos para apoio na composição de endereços.</li>
  <li>Criação de dataset em estrutura tabular.</li>
  <li>Possibilidade de uso do dataset gerado em testes, análises e estudos.</li>
  <li>Apoio a estudos relacionados a Banco de Dados, Big Data e sistemas de informação em saúde.</li>
</ol>

---

## Tecnologias e Conceitos Utilizados

<ol>
  <li>Python</li>
  <li>Google Colab</li>
  <li>Pandas</li>
  <li>Manipulação de dados</li>
  <li>Geração de dados sintéticos</li>
  <li>Criação de datasets</li>
  <li>Banco de Dados</li>
  <li>Big Data</li>
  <li>Dados públicos</li>
  <li>Sistemas de informação em saúde</li>
</ol>

---

## Exemplo de Dados Gerados

<p>
  O dataset gerado pode conter campos semelhantes aos listados abaixo:
</p>

<table>
  <tr>
    <th>Campo</th>
    <th>Descrição</th>
  </tr>
  <tr>
    <td>Nome</td>
    <td>Nome completo gerado de forma sintética.</td>
  </tr>
  <tr>
    <td>CPF</td>
    <td>Número de CPF fictício utilizado apenas para testes.</td>
  </tr>
  <tr>
    <td>RG</td>
    <td>Número de RG fictício utilizado apenas para composição cadastral.</td>
  </tr>
  <tr>
    <td>Estado Civil</td>
    <td>Estado civil simulado para o cadastro da pessoa.</td>
  </tr>
  <tr>
    <td>Nome do Pai</td>
    <td>Nome gerado de forma sintética para composição familiar.</td>
  </tr>
  <tr>
    <td>Nome da Mãe</td>
    <td>Nome gerado de forma sintética para composição familiar.</td>
  </tr>
  <tr>
    <td>Gênero</td>
    <td>Informação demográfica simulada.</td>
  </tr>
  <tr>
    <td>Idade</td>
    <td>Idade gerada para compor o perfil cadastral.</td>
  </tr>
  <tr>
    <td>Endereço</td>
    <td>Informação de endereço composta com apoio de dados públicos.</td>
  </tr>
</table>

---

## Possíveis Aplicações

<p>
  Embora o projeto tenha sido desenvolvido com finalidade acadêmica, ele pode servir como base de estudo para diferentes cenários, como:
</p>

<ol>
  <li>Testes de sistemas de informação.</li>
  <li>Validação de estruturas de banco de dados.</li>
  <li>Criação de bases simuladas para desenvolvimento.</li>
  <li>Estudos de modelagem de dados.</li>
  <li>Testes de relatórios e dashboards.</li>
  <li>Simulações em sistemas de saúde.</li>
  <li>Estudos com Python e Pandas.</li>
  <li>Projetos acadêmicos envolvendo dados demográficos.</li>
  <li>Criação de datasets para ambientes de teste.</li>
</ol>

---

## Como Executar

<p>
  Como o projeto foi desenvolvido inicialmente no Google Colab, recomenda-se executar o código nesse ambiente para reduzir a necessidade de ajustes.
</p>

<p>
  Caso queira executar localmente, siga uma estrutura semelhante:
</p>

<ol>
  <li>
    Clone este repositório:
  </li>
</ol>

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
