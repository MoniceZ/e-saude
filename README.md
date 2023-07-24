# E-Saúde - Gerador de Dados e Dataset

## Explicações por item/arquivo:

<ol>
  <li>ceps_reias: é uma lista de ceps para buscar o endereços na API do POSTMON, utilizar no "gerador-de-dados.py</li>
  
  <li>temp_datafrema: é uma dataset já pronto, para poder verificar o resultador obtido</li>
  
  <li>dataset: é a junção de dois datasets, um de nomes, cpfs, estado civil, pai, mãe, etc + dataset de um de endereços públicos</li>
  
  <li>gerador-dataset: é a primeira versão do código, fucional, porém é necessário utilizar o arquivo "ceps_reais" e do dataset dos endereços prúblicos</li>
  
  <li>gerador-de-dados: é mais completo que o gerador de dataset, mesmo assim, é necessário a utilização do arquivo "ceps_reais".</li>
</ol>

## Explicações de Particularidades

<ol>
  <li>No dataset.py, a URL 1, as vezes, o link está quebrando faça o seguinte, quando isso ocorrer:</li>  
</ol>

<p>
     Abra o link em um página web, peça para reparar seu download, copie o link do download direto.<br />
     Veja o passo a passo: <br />
</p>
     
<p float="center">

 <img src="https://user-images.githubusercontent.com/113941301/255600779-0f4661fc-2e92-4792-906d-5e9ca35654e2.JPG" width="450" />
 <img src="https://user-images.githubusercontent.com/113941301/255603356-1ea53ad1-e145-4c6a-bd84-ee04d4802e03.JPG" width="350" />
 <img src="https://user-images.githubusercontent.com/113941301/255603480-d390afea-ef7c-41d1-b13a-c8c5fabe307b.JPG" width="450" />

</p>
