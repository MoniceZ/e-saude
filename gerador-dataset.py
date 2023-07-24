!pip install faker

import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('pt_BR')

def gerar_nome_completo():
    nome = fake.first_name_male()  # Sempre gera um nome masculino
    sobrenome1 = fake.last_name()
    sobrenome2 = fake.last_name()

    # Verifica se sobrenome1 é igual a sobrenome2 e gera um novo sobrenome2 até que sejam diferentes
    while sobrenome1 == sobrenome2:
        sobrenome2 = fake.last_name()

    genero = 'Masculino'  # Define o gênero como masculino
    data_nascimento = gerar_data_nascimento()

    pai = gerar_nome_pai(genero, sobrenome1, sobrenome2)
    data_nascimento_pai = gerar_data_nascimento_pai(data_nascimento)
    mae = gerar_nome_mae(sobrenome1, sobrenome2)
    data_nascimento_mae = gerar_data_nascimento_mae(data_nascimento)
    estado_civil_filho = gerar_estado_civil_filho(data_nascimento)

    return {
        'nome': nome,
        'sobrenome1': sobrenome1,
        'sobrenome2': sobrenome2,
        'genero': genero,
        'data_nascimento': data_nascimento.strftime('%d/%m/%Y'),
        'pai': pai,
        'data_nascimento_pai': data_nascimento_pai.strftime('%d/%m/%Y'),
        'mae': mae,
        'data_nascimento_mae': data_nascimento_mae.strftime('%d/%m/%Y'),
        'estado_civil_filho': estado_civil_filho
    }

def gerar_nome_pai(genero, sobrenome1_filho, sobrenome2_filho):
    if random.random() < 0.06:
        return "AUSENTE"

    sobrenome_pai = sobrenome1_filho if random.random() < 0.7 else sobrenome2_filho
    sobrenome1_pai = fake.last_name()
    sobrenome2_pai = fake.last_name()

    # Verifica se sobrenome1_pai é igual a sobrenome2_pai e gera um novo sobrenome2_pai até que sejam diferentes
    while sobrenome1_pai == sobrenome2_pai:
        sobrenome2_pai = fake.last_name()

    nome_pai = fake.first_name_male()

    return f"{nome_pai} {sobrenome_pai} {sobrenome1_pai} {sobrenome2_pai}"

def gerar_nome_mae(sobrenome1_filho, sobrenome2_filho):
    # Gera um nome de mãe aleatório com base nos sobrenomes do filho
    sobrenome_mae = sobrenome1_filho if random.random() < 0.7 else sobrenome2_filho
    sobrenome1_mae = fake.last_name()
    sobrenome2_mae = fake.last_name()

    # Verifica se sobrenome1_mae é igual a sobrenome2_mae e gera um novo sobrenome2_mae até que sejam diferentes
    while sobrenome1_mae == sobrenome2_mae:
        sobrenome2_mae = fake.last_name()

    nome_mae = fake.first_name_female()

    return f"{nome_mae} {sobrenome_mae} {sobrenome1_mae} {sobrenome2_mae}"

def gerar_estado_civil_filho(data_nascimento):
    idade = (datetime.now() - data_nascimento).days // 365

    if idade < 18:
        if 16 <= idade < 18 and random.random() < 0.02:
            return "Casado(a)"
        else:
            return "Solteiro(a)"

    estado_civil = random.choices(['Casado(a)', 'Divorciado(a)', 'Viúvo(a)', 'Solteiro(a)'], [0.45, 0.16, 0.04, 0.35])[0]
    return estado_civil

def gerar_data_nascimento():
    # Gera uma data de nascimento aleatória entre 1 de janeiro de 1970 e 31 de dezembro de 2020
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2020, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_data_nascimento_pai(random_date_filho):
    end_date = random_date_filho - timedelta(days=17*365)
    start_date = end_date - timedelta(days=34*365)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_data_nascimento_mae(random_date_filho):
    end_date = random_date_filho - timedelta(days=16*365)
    start_date = end_date - timedelta(days=26*365)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_nomes_quantidade(quantidade):
    nomes_gerados = []
    for _ in range(quantidade):
        nome_completo = gerar_nome_completo()
        nomes_gerados.append(nome_completo)
    return nomes_gerados

# Exemplo de uso
quantidade_desejada = 49
nomes_gerados = gerar_nomes_quantidade(quantidade_desejada)

# Nome do arquivo CSV a ser gerado
nome_arquivo = 'nomes_masculinos.csv'

# Cria o arquivo CSV e escreve os dados gerados nele
with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=['Nome', 'Gênero', 'Data de Nascimento', 'Pai', 'Data de Nascimento do Pai', 'Mãe', 'Data de Nascimento da Mãe', 'Estado Civil do Filho'])
    writer.writeheader()
    for nome in nomes_gerados:
        writer.writerow({'Nome': f"{nome['nome']} {nome['sobrenome1']} {nome['sobrenome2']}",
                         'Gênero': nome['genero'],
                         'Data de Nascimento': nome['data_nascimento'],
                         'Pai': nome['pai'],
                         'Data de Nascimento do Pai': nome['data_nascimento_pai'],
                         'Mãe': nome['mae'],
                         'Data de Nascimento da Mãe': nome['data_nascimento_mae'],
                         'Estado Civil do Filho': nome['estado_civil_filho']})

print(f'O arquivo "{nome_arquivo}" foi gerado com sucesso!')

import csv
import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('pt_BR')

def gerar_nome_completo():
    nome = fake.first_name_female()  # Sempre gera um nome feminino
    sobrenome1 = fake.last_name()
    sobrenome2 = fake.last_name()

    # Verifica se sobrenome1 é igual a sobrenome2 e gera um novo sobrenome2 até que sejam diferentes
    while sobrenome1 == sobrenome2:
        sobrenome2 = fake.last_name()

    genero = 'Feminino'  # Define o gênero como Feminino
    data_nascimento = gerar_data_nascimento()

    pai = gerar_nome_pai(genero, sobrenome1, sobrenome2)
    data_nascimento_pai = gerar_data_nascimento_pai(data_nascimento)
    mae = gerar_nome_mae(sobrenome1, sobrenome2)
    data_nascimento_mae = gerar_data_nascimento_mae(data_nascimento)
    estado_civil_filho = gerar_estado_civil_filho(data_nascimento)

    return {
        'nome': nome,
        'sobrenome1': sobrenome1,
        'sobrenome2': sobrenome2,
        'genero': genero,
        'data_nascimento': data_nascimento.strftime('%d/%m/%Y'),
        'pai': pai,
        'data_nascimento_pai': data_nascimento_pai.strftime('%d/%m/%Y'),
        'mae': mae,
        'data_nascimento_mae': data_nascimento_mae.strftime('%d/%m/%Y'),
        'estado_civil_filho': estado_civil_filho
    }

def gerar_nome_pai(genero, sobrenome1_filho, sobrenome2_filho):
    if random.random() < 0.06:
        return "AUSENTE"

    sobrenome_pai = sobrenome1_filho if random.random() < 0.7 else sobrenome2_filho
    sobrenome1_pai = fake.last_name()
    sobrenome2_pai = fake.last_name()

    # Verifica se sobrenome1_pai é igual a sobrenome2_pai e gera um novo sobrenome2_pai até que sejam diferentes
    while sobrenome1_pai == sobrenome2_pai:
        sobrenome2_pai = fake.last_name()

    nome_pai = fake.first_name_male()

    return f"{nome_pai} {sobrenome_pai} {sobrenome1_pai} {sobrenome2_pai}"

def gerar_nome_mae(sobrenome1_filho, sobrenome2_filho):
    # Gera um nome de mãe aleatório com base nos sobrenomes do filho
    sobrenome_mae = sobrenome1_filho if random.random() < 0.7 else sobrenome2_filho
    sobrenome1_mae = fake.last_name()
    sobrenome2_mae = fake.last_name()

    # Verifica se sobrenome1_mae é igual a sobrenome2_mae e gera um novo sobrenome2_mae até que sejam diferentes
    while sobrenome1_mae == sobrenome2_mae:
        sobrenome2_mae = fake.last_name()

    nome_mae = fake.first_name_female()

    return f"{nome_mae} {sobrenome_mae} {sobrenome1_mae} {sobrenome2_mae}"

def gerar_estado_civil_filho(data_nascimento):
    idade = (datetime.now() - data_nascimento).days // 365

    if idade < 18:
        if 16 <= idade < 18 and random.random() < 0.02:
            return "Casado(a)"
        else:
            return "Solteiro(a)"

    estado_civil = random.choices(['Casado(a)', 'Divorciado(a)', 'Viúvo(a)', 'Solteiro(a)'], [0.45, 0.16, 0.04, 0.35])[0]
    return estado_civil

def gerar_data_nascimento():
    # Gera uma data de nascimento aleatória entre 1 de janeiro de 1970 e 31 de dezembro de 2020
    start_date = datetime(1970, 1, 1)
    end_date = datetime(2020, 12, 31)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_data_nascimento_pai(random_date_filho):
    end_date = random_date_filho - timedelta(days=17*365)
    start_date = end_date - timedelta(days=34*365)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_data_nascimento_mae(random_date_filho):
    end_date = random_date_filho - timedelta(days=16*365)
    start_date = end_date - timedelta(days=26*365)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date

def gerar_nomes_quantidade(quantidade):
    nomes_gerados = []
    for _ in range(quantidade):
        nome_completo = gerar_nome_completo()
        nomes_gerados.append(nome_completo)
    return nomes_gerados

# Exemplo de uso
quantidade_desejada = 100
nomes_gerados = gerar_nomes_quantidade(quantidade_desejada)

# Nome do arquivo CSV a ser gerado
nome_arquivo = 'nomes_femininos.csv'

# Cria o arquivo CSV e escreve os dados gerados nele
with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=['Nome', 'Gênero', 'Data de Nascimento', 'Pai', 'Data de Nascimento do Pai', 'Mãe', 'Data de Nascimento da Mãe', 'Estado Civil do Filho'])
    writer.writeheader()
    for nome in nomes_gerados:
        writer.writerow({'Nome': f"{nome['nome']} {nome['sobrenome1']} {nome['sobrenome2']}",
                         'Gênero': nome['genero'],
                         'Data de Nascimento': nome['data_nascimento'],
                         'Pai': nome['pai'],
                         'Data de Nascimento do Pai': nome['data_nascimento_pai'],
                         'Mãe': nome['mae'],
                         'Data de Nascimento da Mãe': nome['data_nascimento_mae'],
                         'Estado Civil do Filho': nome['estado_civil_filho']})

print(f'O arquivo "{nome_arquivo}" foi gerado com sucesso!')

import csv
from faker import Faker

fake = Faker('pt_BR')

def gerar_cpf_fake(cpfs_gerados):
    cpf = fake.cpf()
    while cpf in cpfs_gerados:  # Verifica se o CPF já foi gerado
        cpf = fake.cpf()
    return cpf

def gerar_cpf_quantidade(quantidade):
    cpfs_gerados = []
    for _ in range(quantidade):
        cpf = gerar_cpf_fake(cpfs_gerados)
        cpfs_gerados.append(cpf)
    return cpfs_gerados

# Exemplo de uso
quantidade_desejada = 100
cpfs_gerados = gerar_cpf_quantidade(quantidade_desejada)

# Nome do arquivo CSV a ser gerado
nome_arquivo = 'cpfs.csv'

# Cria o arquivo CSV e escreve os dados gerados nele
with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['CPF'])
    writer.writerows([[cpf] for cpf in cpfs_gerados])

print(f'O arquivo "{nome_arquivo}" foi gerado com sucesso!')

import pandas as pd

# Caminho do arquivo CSV no Colab
caminho_arquivo = '/content/ceps_reais.csv'

# Ler o arquivo CSV
data_frame = pd.read_csv(caminho_arquivo)

import pandas as pd
import random
import requests
import time
import json
from multiprocessing import Pool

def obter_endereco(cep):
    cep = str(cep)
    time.sleep(0.1)

    try:
        endereco = requests.get(f'https://api.postmon.com.br/v1/cep/{cep}').json()
    except json.JSONDecodeError:
        print(f"Erro ao obter endereço para o CEP {cep}. Pulando para o próximo.")
        return None

    return endereco

def obter_ddd_por_estado(estado):
    ddds = {
        'SP': ['11', '12', '13', '14', '15', '16', '17', '18', '19'],
        'RJ': ['21', '22', '24'],
        'MG': ['31', '32', '33', '34', '35', '37', '38'],
        'ES': ['27', '28'],
        'PR': ['41', '42', '43', '44', '45', '46'],
        'SC': ['47', '48', '49'],
        'RS': ['51', '53', '54', '55'],
        'GO': ['62', '64'],
        'DF': ['61'],
        'MT': ['65', '66'],
        'MS': ['67'],
        'AL': ['82'],
        'BA': ['71', '73', '74', '75', '77'],
        'CE': ['85', '88'],
        'MA': ['98', '99'],
        'PB': ['83'],
        'PE': ['81', '87'],
        'PI': ['86', '89'],
        'RN': ['84'],
        'SE': ['79'],
        'AC': ['68'],
        'AP': ['96'],
        'AM': ['92', '97'],
        'PA': ['91', '93', '94'],
        'RO': ['69'],
        'RR': ['95'],
        'TO': ['63']
    }

    # Retornar um DDD padrão caso o estado não esteja no dicionário
    return ddds.get(estado, ['00'])

def gerar_telefone_fixo(ddd):
    telefone = str(random.randint(30000000, 49999999))
    return f'({ddd}) {telefone[:4]}-{telefone[4:]}'

def gerar_telefone_celular(ddd):
    telefone = str(random.randint(900000000, 999999999))
    return f'({ddd}) {telefone[0]}.{telefone[1:5]}-{telefone[5:]}'

def gerar_enderecos(ceps):
    enderecos = []
    ceps_utilizados = set()
    ceps_invalidos = set()

    with Pool(processes=50) as pool:  # Altere o número de processos conforme necessário
        results = pool.map(obter_endereco, ceps)

    for endereco in results:
        if endereco is None or 'cep' not in endereco:
            continue

        cep = endereco['cep']
        if 'erro' in endereco or cep in ceps_utilizados or cep in ceps_invalidos:
            ceps_invalidos.add(cep)
            continue

        rua = endereco['logradouro']
        numero = random.randint(0, 9999)
        if numero == 0:
            numero = "S/N"
        bairro = endereco['bairro']
        cidade = endereco['cidade']
        estado = endereco['estado']
        complemento = endereco.get('complemento', '')

        ddds = obter_ddd_por_estado(estado)
        ddd = random.choice(ddds)

        if random.choice([True, False]):
            telefone = gerar_telefone_fixo(ddd)
        else:
            telefone = gerar_telefone_celular(ddd)

        enderecos.append((rua, numero, bairro, complemento, cidade, estado, cep, telefone))
        ceps_utilizados.add(cep)

    return enderecos

# Obter os valores da coluna desejada
coluna = data_frame['CEPs']
# Converter a coluna em uma lista
lista_valores = coluna.tolist()

# Definir o número de valores a serem sorteados
num_valores_sorteados = 5

# Realizar o sorteio sem repetições
valores_sorteados = random.sample(lista_valores, num_valores_sorteados)

ceps_sorteados = [str(s).replace('-', '').strip() for s in valores_sorteados]

enderecos = gerar_enderecos(ceps_sorteados)

# Criar um DataFrame pandas com os endereços
df = pd.DataFrame(enderecos, columns=['Rua', 'Número', 'Bairro', 'Complemento', 'Cidade', 'Estado', 'CEP', 'Telefone'])

# Exportar o DataFrame para um arquivo CSV UTF-8
df.to_csv('enderecos.csv', index=False, encoding='utf-8-sig')

print('Arquivo enderecos.csv exportado com sucesso!')

##importando bibliotecas pandas, matplotlib e zipfile
# pandas --> preprocessing
# matoplotlib --> data visualization
# zipfile --> to manipulate zip files

import pandas as pd

import matplotlib.pyplot as plt

import zipfile

## abrindo a base de dados do prof Ivan R Zimmermam no colab
## https://data.mendeley.com/datasets/g97jb8fp57/1


url = "https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/g97jb8fp57-1.zip"

df = pd.read_csv(url,sep=('\t'))

df

# separando a coluna do arquivo zip em colunas
# aula https://www.youtube.com/watch?v=TJfi2rLecO4&t=74s

df['CEP;UF;CIDADE;BAIRRO;LOGRADOURO;COMPLEMENTO'].str.split(';', expand=True)

# separando a coluna do arquivo zip em colunas, por título

df[['CEP','UF','CIDADE','BAIRRO','LOGRADOURO','COMPLEMENTO','a','b']] = df['CEP;UF;CIDADE;BAIRRO;LOGRADOURO;COMPLEMENTO'].str.split(';', expand=True)

df

df[['CEP', 'UF', 'CIDADE',
       'BAIRRO', 'LOGRADOURO', 'COMPLEMENTO']]

df2 = df[['CEP', 'UF', 'CIDADE',
       'BAIRRO', 'LOGRADOURO', 'COMPLEMENTO']]

df2

df2.describe()
