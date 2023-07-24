# E-Saúde - Gerador de Dados e Dataset

## Explicações por item/arquivo:

<ol>
  <li><img src="https://user-images.githubusercontent.com/113941301/255662747-df74a21e-221c-4b3c-b74e-03a43ac6f731.png" width="15" /><strong> ceps_reias:</strong> é uma lista de ceps para buscar o endereços na API do POSTMON, utilizar no "gerador-de-dados.py</li>
  
  <li><img src="https://user-images.githubusercontent.com/113941301/255662747-df74a21e-221c-4b3c-b74e-03a43ac6f731.png](https://user-images.githubusercontent.com/113941301/255663474-ecaa9790-73ef-4d95-a72e-61346b753338.jpg)" width="15" /><strong>temp_dataframe:</strong> é uma dataset já pronto, para poder verificar o resultador obtido</li>
  
  <li><strong>dataset.py:</strong> é a junção de duas bases de dados. A primeira contém dados de nomes de pessoas com CPF, estado civil, nome do pai, nome da mãe, etc. A segunda apresenta uma lista de CEPs e a descrição dos endereços correspondentes.</li>
  
  <li><strong>gerador-dataset:</strong> é a primeira versão do código, fucional, porém é necessário utilizar o arquivo "ceps_reais" e da lista dos endereços</li>
  
  <li><strong>gerador-de-dados:</strong> é mais completo que o gerador de dataset, mesmo assim, é necessário a utilização do arquivo "ceps_reais".</li>
</ol>

## Explicações de Particularidades

<ol>
  <li>No dataset.py, a URL 1, as vezes, o link está quebrando, faça o seguinte, quando isso ocorrer:</li>  

<p>Abra o link em um página web, peça para reparar seu download, copie o link do download direto.<br /></p>
<p>Veja o passo a passo: <br /></p>

     
<p align="center">

 <img src="https://user-images.githubusercontent.com/113941301/255600779-0f4661fc-2e92-4792-906d-5e9ca35654e2.JPG" width="450" />
 <img src="https://user-images.githubusercontent.com/113941301/255603356-1ea53ad1-e145-4c6a-bd84-ee04d4802e03.JPG" width="350" />
 <img src="https://user-images.githubusercontent.com/113941301/255603480-d390afea-ef7c-41d1-b13a-c8c5fabe307b.JPG" width="450" />

</p>

<p>
  <li>Como todo o código foi desenvolvido no Colab, pode ser quer se ao tentar executa-lo em seu ambiente, precise reorganiza-lo.</li>
</p>
<li>Quando tenta abrir o dataset já pronto, o Excel não suporta a quantidade de dados, ele chega abrir o arquivo, mas se perde algumas linhas.</li>

</ol>

## Limitações

<p>Quando falamos de sobrenomes, é algo complexo, pois levamos em conta o seguintes fatores:</p>

<ol>
<li>Sobrenome1 não pode ser igual ao Sobrenome2</li>
<li>Sobrenome1 e Sobrenome2 do Filho pode ou não ser igual o do pai ou da mãe, ou simplesmente só um sobrenome ser igual de um dos pais</li>
<li>Sobrenome1 e Sobrenome2 pode ou não ser iguais entre pai e mãe, podendo ser diferentes tamvém, ou somente um igual</li>
</ol>

<p>Porém, essas limitações que ainda não foram completamente resolvidas</p>

<ul>
  <li>Ocorreu sobrenome1 = sobrenome2</li>
  <li>Ocorreu do filho nunca ter sobrenomes dos pais</li>
  <li>Ocorreu dos sobrenomes do pais sempre ou nunca serem iguais</li>
</ul>

## Objetivo desse trabalho
<p>
O objetivo geral é desenvolver uma solução para a geração e/ou armazenamento de dados demográficos para teste em sistema de informação. Esta solução visa fornecer informações precisas sobre pacientes, incluindo gênero, idade, endereço e outras características.
</p>

### Sinta-se livre para ajudar, com comentários, códigos, lógicas, etc.

<br />
<p align="right"><b>Criado por:</b></p>
<p align="right">Fábio Monice</p>
<p align="right">Eliana Mendes</p>

<br />
<p align="right"><b>Orientado por:</b></p>
<p align="right">
  <a href="https://ww2.inf.ufg.br/node/118">Professor Iwens Sene</a>
</p>

