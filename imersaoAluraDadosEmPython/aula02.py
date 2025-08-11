import pandas
import numpy
nomes = ["Ana Silva", "Bruno Costa", "Carla Souza", "Daniel Lima", "Eduarda Martins", "Felipe Alves", "Gabriela Rocha", "Henrique Dias", "Isabela Pinto", "João Mendes", "Lucas Ferrari"]

dataframeSalarios = pandas.DataFrame({
    'nome': nomes,
    'salarios': [
        4500,
        numpy.nan,
        4800,
        6000,
        numpy.nan,
        5300,
        4900,
        numpy.nan,
        5500,
        numpy.nan,
        100000
    ]
})
#media
dataframeSalarios['salarioMedia'] = dataframeSalarios['salarios'].fillna(dataframeSalarios['salarios'].mean().round(2))

#mediana
dataframeSalarios['salarioMediano'] = dataframeSalarios['salarios'].fillna(dataframeSalarios['salarios'].median())

dataframeTemperaturas = pandas.DataFrame({
    'dia': [
        "Segunda",
        "Terça",
        "Quarta",
        "Quinta",
        "Sexta",
        "Sábado",
        "Domingo"
    ],
    'temperatura': [
        22.5,
        numpy.nan,
        21.8,
        24.1,
        25.0,
        23.5,
        numpy.nan
    ]
})
dataframeTemperaturas['preenchido_ffill'] = dataframeTemperaturas['temperatura'].ffill()
dataframeTemperaturas['preenchido_bfill'] = dataframeTemperaturas['temperatura'].bfill()

dataframeCidades = pandas.DataFrame({
    'nome': nomes,
    'cidade': [
        "São Paulo",
        "Rio de Janeiro",
        "Belo Horizonte",
        numpy.nan,
        "Porto Alegre",
        "Recife",
        "Salvador",
        numpy.nan,
        "Fortaleza",
        "Manaus",
        numpy.nan
    ]
})
dataframeCidades['cidade_preenchida'] = dataframeCidades['cidade'].fillna("Nao informado")
print(dataframeCidades.head)