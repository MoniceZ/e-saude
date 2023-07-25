# E-Saúde - Gerador de Dados e Dataset

## Explicações por item/arquivo:

<ol> 
 <li><img src="https://user-images.githubusercontent.com/113941301/255664814-a85bc430-2cb8-4014-a835-eb40367ea459.png" width="15" /><strong> gerador_de_dados:</strong> gera dados de pessoas, como nomes, CPFs, RG, Estado Civil, nome do pai, nome da mãe, etc. </li>
</ol>

## Explicações de Particularidades

<ol>
 
<p>
  <li>Como todo o código foi desenvolvido no Colab, pode ser quer se ao tentar executa-lo em seu ambiente, precise reorganiza-lo.</li>
</p>
<li>Quando tenta abrir o dataset já pronto, o Excel não suporta a quantidade de dados, ele chega abrir o arquivo, mas se perde algumas linhas. </li>

</ol>

## Limitações

<p>Quando falamos de sobrenomes, é algo complexo, pois levamos em conta os seguintes fatores:</p>

<ol>
<li>Sobrenome1 não pode ser igual ao Sobrenome2</li>
<li>Sobrenome1 e Sobrenome2 do Filho pode ou não ser igual o do pai ou da mãe, ou simplesmente só um sobrenome ser igual de um dos pais</li>
<li>Sobrenome1 e Sobrenome2 pode ou não ser iguais entre pai e mãe, podendo ser diferentes também, ou somente um igual</li>
</ol>

<p>Porém, essas limitações que ainda não foram completamente resolvidas</p>

<ul>
  <li>Ocorreu sobrenome1 = sobrenome2</li>
  <li>Ocorreu de o filho nunca ter sobrenomes dos pais</li>
  <li>Ocorreu dos sobrenomes do pais sempre ou nunca serem iguais</li>
</ul>

## Objetivo desse trabalho
<p>
O objetivo geral é desenvolver uma solução para a geração e/ou armazenamento de dados demográficos para teste em sistema de informação. Esta solução visa fornecer informações precisas sobre pacientes, incluindo gênero, idade, endereço e outras características.
</p>

### Sinta-se livre para ajudar, com comentários, códigos, lógicas, etc.

<br />
<p align="right"><b>Criado por:</b></p>
<p align="right">
  <a href="https://www.linkedin.com/in/fabiomonice">Fábio Monice</p>
<p align="right">Eliana Mendes</p>

<br />
<p align="right"><b>Orientado por:</b></p>
<p align="right">
  <a href="https://ww2.inf.ufg.br/node/118">Professor Iwens Sene</a>
</p>

