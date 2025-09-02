import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn

urlDataBase = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
dataframe = pandas.read_csv(urlDataBase)
dataframeLimpo = dataframe.dropna()

plt.figure(figsize=(8,5))

order = dataframeLimpo.groupby('experience_level')['salary_in_usd'].mean().sort_values(ascending=True).index
seaborn.barplot(data=dataframeLimpo, x='experience_level',y='salary_in_usd',order=order)

plt.title('salario medio por senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salario medio anual(USD)')
plt.show()




