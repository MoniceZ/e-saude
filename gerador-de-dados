!pip install faker
!pip install cpf-generator
import random
from faker import Faker
from datetime import datetime, timedelta
from cpf_generator import CPF
import csv
import pandas as pd
from multiprocessing import Pool
import numpy as np
from faker.providers.person.pt_BR import Provider as PtBrProvider
from faker.providers.date_time.pt_BR import Provider as PtBrDateTimeProvider
from faker.providers.internet import Provider as InternetProvider
from faker.providers.ssn.pt_BR import Provider as PtBrSsnProvider

quantidade_geral_de_dados_real = 5000  #Recomendado até 5000
#Testado e Aprovado até 5.000/vez

quantide_geral_de_processos_real = 50 #Recomendado até 50
#Ajuda a otimizar o tempo para geração dos dados, não aumente muito, pode "quebrar" o desempenho real.

fake = Faker(['pt_BR'])

def gerar_genero():
    generos = ['Masculino', 'Feminino']
    chances = [0.49, 0.51]
    return random.choices(generos, chances)[0]

def gerar_nome_sobrenome(genero):
    if genero == 'Masculino':
        nome = fake.first_name_male()
        sobrenome1 = fake.last_name_male()
        sobrenome2 = fake.last_name_male()
    else:
        nome = fake.first_name_female()
        sobrenome1 = fake.last_name_female()
        sobrenome2 = fake.last_name_female()
    return nome, sobrenome1, sobrenome2

def gerar_sobrenomes_raros(quantidade):
    sobrenomes_raros = set()
    while len(sobrenomes_raros) < quantidade:
        sobrenomes_raros.add(fake.last_name())
    return list(sobrenomes_raros)

def gerar_sobrenomes_filho(sobrenomes_pai, sobrenomes_mae):
    sobrenome1_filho = random.choice(sobrenomes_pai + sobrenomes_mae)
    sobrenome2_filho = random.choice([s for s in sobrenomes_pai + sobrenomes_mae if s != sobrenome1_filho])
    return sobrenome1_filho, sobrenome2_filho

def gerar_nome_pai(sobrenomes_raros, data_nascimento_filho):
    idade_minima_pai = 17
    idade_maxima_pai = 50
    data_maxima_pai = data_nascimento_filho - timedelta(days=(idade_minima_pai * 365))
    data_minima_pai = data_nascimento_filho - timedelta(days=(idade_maxima_pai * 365))
    data_nascimento_pai = fake.date_between_dates(date_start=data_minima_pai, date_end=data_maxima_pai)
    nome_pai = fake.first_name_male()

    sobrenomes_pai = random.sample(sobrenomes_raros, k=2)

    return nome_pai, sobrenomes_pai[0], sobrenomes_pai[1], data_nascimento_pai

def gerar_nome_mae(sobrenomes_raros, data_nascimento_filho):
    idade_minima_mae = 16
    idade_maxima_mae = 40
    data_maxima_mae = data_nascimento_filho - timedelta(days=(idade_minima_mae * 365))
    data_minima_mae = data_nascimento_filho - timedelta(days=(idade_maxima_mae * 365))
    data_nascimento_mae = fake.date_between_dates(date_start=data_minima_mae, date_end=data_maxima_mae)
    nome_mae = fake.first_name_female()

    sobrenomes_mae = random.sample(sobrenomes_raros, k=2)

    return nome_mae, sobrenomes_mae[0], sobrenomes_mae[1], data_nascimento_mae

def gerar_data_nascimento_filho(data_nascimento_pai, data_nascimento_mae):
    data_minima = max(data_nascimento_pai, data_nascimento_mae) - timedelta(days=(22 * 365))
    data_maxima = datetime.now().date()
    data_nascimento_filho = fake.date_between_dates(date_start=data_minima, date_end=data_maxima)
    return data_nascimento_filho

def gerar_nome_filho(nome_pai, nome_mae, sobrenomes_raros):
    nome_filho = fake.first_name()
    nome_pai_sem_sobrenome = nome_pai.split(' ')[0]
    nome_mae_sem_sobrenome = nome_mae.split(' ')[0]
    sobrenome1_filho, sobrenome2_filho = gerar_sobrenomes_filho([nome_pai_sem_sobrenome, nome_mae_sem_sobrenome], sobrenomes_raros)
    return f"{nome_filho} {sobrenome1_filho} {sobrenome2_filho}"

def gerar_rg():
    rg = str(fake.random_number(digits=7)).zfill(7)  # Garante que o RG tenha sempre 7 dígitos
    return f"{rg}"

def gerar_registro(_):
    genero = gerar_genero()
    rg_filho = gerar_rg()
    nome_pai, sobrenomes_pai1, sobrenomes_pai2, data_nascimento_pai = gerar_nome_pai(sobrenomes_raros, datetime.now().date())
    nome_mae, sobrenomes_mae1, sobrenomes_mae2, data_nascimento_mae = gerar_nome_mae(sobrenomes_raros, datetime.now().date())

    sobrenomes_raros.extend([sobrenomes_pai1, sobrenomes_pai2, sobrenomes_mae1, sobrenomes_mae2])

    data_nascimento_filho = gerar_data_nascimento_filho(data_nascimento_pai, data_nascimento_mae)
    nome_filho = gerar_nome_filho(nome_pai, nome_mae, sobrenomes_raros)

    # Adicionando as probabilidades para o estado civil
    estado_civil_probabilidades = ('Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)')
    estado_civil_chances = [42.8, 45.8, 6, 5.4]
    estado_civil_filho = np.random.choice(estado_civil_probabilidades, p=(estado_civil_chances / np.sum(estado_civil_chances)))

    cpf_filho = fake.random_number(digits=11)

    return {
        'Nome do Filho(a)': nome_filho,
        'Gênero': genero,
        'RG': rg_filho,
        'CPF': cpf_filho,
        'Data de Nascimento Filho(a)': data_nascimento_filho.strftime('%d/%m/%Y'),
        'Estado Civil': estado_civil_filho,
        'Pai': f"{nome_pai} {sobrenomes_pai1} {sobrenomes_pai2}",
        'Data de Nascimento Pai': data_nascimento_pai.strftime('%d/%m/%Y'),
        'Mãe': f"{nome_mae} {sobrenomes_mae1} {sobrenomes_mae2}",
        'Data de Nascimento Mãe': data_nascimento_mae.strftime('%d/%m/%Y')
    }


if __name__ == '__main__':
    quantidade_geral_de_dados = 100  # Número de registros que você deseja gerar
    quantidade_geral_de_processos = 4  # Número de processos para o multiprocessing

    sobrenomes_raros = gerar_sobrenomes_raros(50)

    with Pool(processes=quantidade_geral_de_processos) as pool:
        registros = pool.map(gerar_registro, range(quantidade_geral_de_dados))

    # Fechamento do pool de processos
    pool.close()
    # Aguarda a finalização de todos os processos
    pool.join()

    # Exportar para CSV formatado em UTF-8
    nome_arquivo = 'registros.csv'

    with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=['Nome do Filho(a)', 'Gênero', 'RG', 'CPF', 'Data de Nascimento Filho(a)', 'Estado Civil', 'Pai', 'Data de Nascimento Pai', 'Mãe', 'Data de Nascimento Mãe'])
        writer.writeheader()
        for registro in registros:
            # Convert RG to string with leading zeros before writing to the CSV
            registro['RG'] = str(registro['RG']).zfill(7)
            writer.writerow(registro)

    print(f'{quantidade_geral_de_dados} registros foram gerados e exportados para {nome_arquivo}.')

# Caminho do arquivo CSV no Colab
caminho_arquivo = '/content/ceps_reais.csv'

# Ler o arquivo CSV
data_frame = pd.read_csv(caminho_arquivo)

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

    with Pool(processes=quantide_geral_de_processos) as pool:  # Altere o número de processos conforme necessário
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
num_valores_sorteados = quantidade_geral_de_dados

# Realizar o sorteio sem repetições
valores_sorteados = random.sample(lista_valores, num_valores_sorteados)

ceps_sorteados = [str(s).replace('-', '').strip() for s in valores_sorteados]

enderecos = gerar_enderecos(ceps_sorteados)

# Criar um DataFrame pandas com os endereços
df = pd.DataFrame(enderecos, columns=['Rua', 'Número', 'Bairro', 'Complemento', 'Cidade', 'Estado', 'CEP', 'Telefone'])

# Exportar o DataFrame para um arquivo CSV UTF-8
df.to_csv('enderecos.csv', index=False, encoding='utf-8-sig')

print('Arquivo enderecos.csv exportado com sucesso!')

# Carregar o arquivo CSV de registros de filhos
df_registros = pd.read_csv('registros.csv')

# Carregar o arquivo CSV de endereços
df_enderecos = pd.read_csv('enderecos.csv')

# Realizar a junção dos DataFrames pelos índices
df_combinado = pd.concat([df_registros, df_enderecos], axis=1)

# Exportar o DataFrame combinado para um novo arquivo CSV
df_combinado.to_csv('dados_combinados.csv', index=False, encoding='utf-8-sig')

print('Arquivo dados_combinados.csv exportado com sucesso!')
