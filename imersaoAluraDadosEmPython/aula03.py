import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn

translatePortuguese = {
            'SE': 'Senior',
            'MI': 'Junior',
            'EN': 'Pleno',
            'EX': 'Executivo'
        }

urlDataBase = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
dataframe = pandas.read_csv(urlDataBase)
dataframeLimpo = dataframe.dropna()
dataframeLimpo = dataframeLimpo.assign(work_year = dataframeLimpo['work_year'].astype('int64'))
dataframeLimpo['experience_level'] = dataframeLimpo["experience_level"].map(translatePortuguese)

dataframeLimpo['experience_level'].value_counts().plot(kind='bar', title="Distribuição de senioridade")

order = dataframeLimpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=True).index

seaborn.barplot(data=dataframeLimpo, x='experience_level', y='salary_in_usd',order=order)



