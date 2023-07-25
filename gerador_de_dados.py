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
    available_sobrenomes = [s for s in sobrenomes_pai + sobrenomes_mae if s != sobrenome1_filho]
    
    if available_sobrenomes:
        sobrenome2_filho = random.choice(available_sobrenomes)
    else:
        sobrenome2_filho = ""
    
    return sobrenome1_filho, sobrenome2_filho

def gerar_nome_pai(sobrenomes_raros, data_nascimento_filho):
    idade_minima_pai = 17
    idade_maxima_pai = 50
    data_maxima_pai = data_nascimento_filho - timedelta(days=(idade_minima_pai * 365))
    data_minima_pai = data_nascimento_filho - timedelta(days=(idade_maxima_pai * 365))
    data_nascimento_pai = fake.date_between_dates(date_start=data_minima_pai, date_end=data_maxima_pai)
    data_nascimento_pai -= timedelta(days=(17 * 365))  # Garante que o pai tenha pelo menos 17 anos a mais que o filho
    nome_pai = fake.first_name_male()

    sobrenomes_pai = random.sample(sobrenomes_raros, k=min(2, len(sobrenomes_raros)))

    return (nome_pai, sobrenomes_pai, data_nascimento_pai)

def gerar_nome_mae(sobrenomes_raros, data_nascimento_filho):
    idade_minima_mae = 16
    idade_maxima_mae = 40
    data_maxima_mae = data_nascimento_filho - timedelta(days=(idade_minima_mae * 365))
    data_minima_mae = data_nascimento_filho - timedelta(days=(idade_maxima_mae * 365))
    data_nascimento_mae = fake.date_between_dates(date_start=data_minima_mae, date_end=data_maxima_mae)
    data_nascimento_mae -= timedelta(days=(16 * 365))  # Garante que a mãe tenha pelo menos 16 anos a mais que o filho
    nome_mae = fake.first_name_female()

    sobrenomes_mae = random.sample(sobrenomes_raros, k=min(2, len(sobrenomes_raros)))

    return (nome_mae, sobrenomes_mae, data_nascimento_mae)

def gerar_data_nascimento_filho(data_nascimento_pai, data_nascimento_mae):
    data_minima = max(data_nascimento_pai, data_nascimento_mae) - timedelta(days=(22 * 365))
    data_maxima = datetime.now().date()
    data_nascimento_filho = fake.date_between_dates(date_start=data_minima, date_end=data_maxima)
    return data_nascimento_filho

def gerar_nome_filho(nome_pai, nome_mae, sobrenomes_raros, genero):
    if genero == 'Masculino':
        nome_filho = fake.first_name_male()
    else:
        nome_filho = fake.first_name_female()

    sobrenomes_pai = nome_pai[1]
    sobrenomes_mae = nome_mae[1]

    if not sobrenomes_pai and not sobrenomes_mae:
        return f"{nome_filho}", "", ""

    if not sobrenomes_pai or not sobrenomes_mae:
        sobrenome1_filho = sobrenomes_pai[0] if sobrenomes_pai else sobrenomes_mae[0]
        sobrenome2_filho = ""
    else:
        sobrenome1_filho, sobrenome2_filho = gerar_sobrenomes_filho(sobrenomes_pai, sobrenomes_mae)

    return f"{nome_filho}", sobrenome1_filho, sobrenome2_filho

def gerar_rg():
    rg = str(fake.random_number(digits=7)).zfill(7)
    return f"{rg}"

def format_cpf(cpf):
    cpf_str = str(cpf).zfill(11)
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

def gerar_registro(_):
    genero = gerar_genero()
    rg_filho = gerar_rg()
    nome_pai = gerar_nome_pai(sobrenomes_raros, datetime.now().date())
    nome_mae = gerar_nome_mae(sobrenomes_raros, datetime.now().date())

    sobrenomes_raros.extend(nome_pai[1])
    sobrenomes_raros.extend(nome_mae[1])

    data_nascimento_filho = gerar_data_nascimento_filho(nome_pai[2], nome_mae[2])
    nome_filho, sobrenome1_filho, sobrenome2_filho = gerar_nome_filho(nome_pai, nome_mae, sobrenomes_raros, genero)

    idade_filho = (datetime.now().date() - data_nascimento_filho).days // 365
    estado_civil_probabilidades = ('Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)')
    if idade_filho < 18:
        estado_civil_chances = [100, 0, 0, 0]
    else:
        estado_civil_chances = [42.8, 45.8, 6, 5.4]

    estado_civil_filho = np.random.choice(estado_civil_probabilidades, p=(estado_civil_chances / np.sum(estado_civil_chances)))

    cpf_filho = fake.random_number(digits=11)
    cpf_filho_formatado = format_cpf(cpf_filho)

    return {
        'Nome do Filho(a)': f"{nome_filho} {sobrenome1_filho} {sobrenome2_filho}",
        'Gênero': genero,
        'RG': rg_filho,
        'CPF': cpf_filho_formatado,
        'Data de Nascimento Filho(a)': data_nascimento_filho.strftime('%d/%m/%Y'),
        'Estado Civil': estado_civil_filho,
        'Pai': f"{nome_pai[0]} {' '.join(nome_pai[1])}",
        'Data de Nascimento Pai': nome_pai[2].strftime('%d/%m/%Y'),
        'Mãe': f"{nome_mae[0]} {' '.join(nome_mae[1])}",
        'Data de Nascimento Mãe': nome_mae[2].strftime('%d/%m/%Y')
    }

if __name__ == '__main__':
    quantidade_geral_de_dados_real = 395306
    quantidade_geral_de_processos_real = 50

    sobrenomes_raros = gerar_sobrenomes_raros(50)

    with Pool(processes=quantidade_geral_de_processos_real) as pool:
        registros = pool.map(gerar_registro, range(quantidade_geral_de_dados_real))

    pool.close()
    pool.join()

    nome_arquivo = 'registros.csv'

    with open(nome_arquivo, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.DictWriter(file, fieldnames=['Nome do Filho(a)', 'Gênero', 'RG', 'CPF', 'Data de Nascimento Filho(a)', 'Estado Civil', 'Pai', 'Data de Nascimento Pai', 'Mãe', 'Data de Nascimento Mãe'])
        writer.writeheader()
        for registro in registros:
            registro['RG'] = str(registro['RG']).zfill(7)
            writer.writerow(registro)

    print(f'{quantidade_geral_de_dados_real} registros foram gerados e exportados para {nome_arquivo}.')
