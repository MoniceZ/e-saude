##importando bibliotecas pandas, matplotlib e zipfile
# pandas --> preprocessing
# matoplotlib --> data visualization
# zipfile --> to manipulate zip files

import pandas as pd

import matplotlib.pyplot as plt

import zipfile

## abrindo a base de dados do prof Ivan R Zimmermam no colab
## https://data.mendeley.com/datasets/g97jb8fp57/1


url1 = "https://download1531.mediafire.com/rvzmj77nl2wgE_5Xx_dKU6V4W0EHqPwh35i3tXueFXo1cHyzNvrq2G17ZzArIe2N0l3-rZYkBPPMgK0GcoZ3ryKzkDtiJUhCuWPQWJqdcvgs9iV-o8hSCrWHqrzZiqQZFFIBJz3vqPjWSEQxoLEIhVqwsxwj8xlcAiW7BDyOwuaJNYA/7tng7xr7yl6v7ji/registros.zip"

url2 = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/g97jb8fp57-1.zip"


df1 = pd.read_csv(url1,sep=('\t'))
df2 = pd.read_csv(url2,sep=('\t'))


df1['Nome do Filho(a),Gênero,CPF,Data de Nascimento Filho(a),Estado Civil,Pai,Data de Nascimento Pai,Mãe,Data de Nascimento Mãe'].str.split(',', expand=True)
df1[['Nome do Filho(a)','Gênero','CPF','Data de Nascimento Filho(a)','Estado Civil','Pai','Data de Nascimento Pai','Mãe','Data de Nascimento Mãe']] = df1['Nome do Filho(a),Gênero,CPF,Data de Nascimento Filho(a),Estado Civil,Pai,Data de Nascimento Pai,Mãe,Data de Nascimento Mãe'].str.split(',', expand=True)
df1[['Nome do Filho(a)','Gênero','CPF','Data de Nascimento Filho(a)','Estado Civil','Pai','Data de Nascimento Pai','Mãe','Data de Nascimento Mãe']]

df2['CEP;UF;CIDADE;BAIRRO;LOGRADOURO;COMPLEMENTO'].str.split(';', expand=True)
df2[['CEP','UF','CIDADE','BAIRRO','LOGRADOURO','COMPLEMENTO','a','b']] = df2['CEP;UF;CIDADE;BAIRRO;LOGRADOURO;COMPLEMENTO'].str.split(';', expand=True)
df2[['CEP', 'UF', 'CIDADE',
       'BAIRRO', 'LOGRADOURO', 'COMPLEMENTO']]

df3 = pd.concat([df1, df2], axis=1)
df3[['Nome do Filho(a)','Gênero','CPF','Data de Nascimento Filho(a)','Estado Civil','Pai',
     'Data de Nascimento Pai','Mãe','Data de Nascimento Mãe',
     'LOGRADOURO', 'COMPLEMENTO', 'BAIRRO', 'CIDADE', 'UF', 'CEP']]

selected_columns = ['Nome do Filho(a)', 'Gênero', 'CPF', 'Data de Nascimento Filho(a)', 'Estado Civil',
                    'Pai', 'Data de Nascimento Pai', 'Mãe', 'Data de Nascimento Mãe',
                    'LOGRADOURO', 'COMPLEMENTO', 'BAIRRO', 'CIDADE', 'UF', 'CEP']
df_selected = df3[selected_columns]

# Salve o DataFrame df_selected em um arquivo CSV temporário
csv_temp_path = '/content/temp_dataframe.csv'  # Substitua pelo caminho desejado
df_selected.to_csv(csv_temp_path, index=False)
