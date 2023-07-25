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
