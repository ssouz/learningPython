from ast import match_case
import pandas

# Fonte dos dados
urlDataBase = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"

# Carrega o DataFrame
dataframe = pandas.read_csv(urlDataBase)

# Menu de opções
print("Escolha uma opção:")
print("1 - Exibir as primeiras linhas do DataFrame")
print("2 - Exibir resumo do DataFrame (info)")
print("3 - Exibir estatísticas descritivas (describe)")
print("4 - Exibir formato do DataFrame (shape)")
print("5 - Traduzir colunas e mostrar contagem de valores")
print("6 - Traduzir tamanho da empresa")

option = input("Digite o número da opção desejada: ")

match option:
    case "1":
        print("\nO método head exibe as primeiras linhas de um DataFrame ou Series.")
        print(dataframe.head(3))

    case "2":
        print("\nO método info exibe um resumo do DataFrame, incluindo tipos de dados, valores não nulos e uso de memória.")
        print(dataframe.info())

    case "3":
        print("\nO método describe retorna estatísticas descritivas para colunas numéricas e resumos para colunas categóricas.")
        print(dataframe.describe())

    case "4":
        print("\nO atributo shape retorna uma tupla: (linhas, colunas).")
        print("Shape:", dataframe.shape)
        print("Linhas:", dataframe.shape[0])
        print("Colunas:", dataframe.shape[1])

    case "5":
        print("\nEvite traduzir colunas diretamente, pois modifica o DataFrame original.")
        print("Colunas originais:", dataframe.columns)

        # Tradução das colunas
        columnTranslation = {
            'work_year': 'ano',
            'experience_level': 'senioridade',
            'employment_type': 'tipo_emprego',
            'job_title': 'cargo',
            'salary': 'salario',
            'salary_currency': 'moeda',
            'salary_in_usd': 'usd',
            'employee_residence': 'residencia',
            'remote_ratio': 'remoto',
            'company_location': 'empresa',
            'company_size': 'tamanho_empresa'
        }
        dataframe.rename(columns=columnTranslation, inplace=True)
        print("Colunas traduzidas:", dataframe.columns)

        # Contagem de valores únicos
        print("\nContagem de valores em 'tamanho_empresa':")
        print(dataframe['tamanho_empresa'].value_counts())

        # Tradução dos valores de senioridade
        traducaoSenioridade = {
            'SE': 'Senior',
            'MI': 'Junior',
            'EN': 'Pleno',
            'EX': 'Executivo'
        }
        dataframe['senioridade'] = dataframe['senioridade'].map(traducaoSenioridade)
        print("\nContagem de valores em 'senioridade':")
        print(dataframe['senioridade'].value_counts())

    case "6":
        # Tradução dos valores de tamanho da empresa
        traducaoTamanhoDaEmpresa = {
            'L': 'Grande porte',
            'M': 'Médio porte',
            'S': 'Pequeno porte'
        }
        dataframe["company_size"] = dataframe["company_size"].map(traducaoTamanhoDaEmpresa)
        print("\nPrimeiras linhas do DataFrame com tamanho da empresa traduzido:")
        print(dataframe.head())