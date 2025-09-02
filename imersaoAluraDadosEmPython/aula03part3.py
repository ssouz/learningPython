import pandas
import matplotlib.pyplot as plt
import seaborn
import plotly.express as plotly


orderExperienceLevel = ['junior','pleno','senior','executivo']
dataframe = pandas.read_csv('https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv').dropna()


plt.figure(figsize=(8,5))
custom_palette = seaborn.color_palette(['#3f6d4e', '#8bd450', '#1d1a2f', '#d62728'])

seaborn.boxplot(x='senioridade',y='usd',data=dataframe,order=orderExperienceLevel, palette=custom_palette, hue='senioridade')

plt.title('boxplot da distribuiçao por senioridade')
plt.xlabel('salario em usd')
plt.show()

