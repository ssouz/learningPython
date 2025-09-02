import pandas
import plotly.express as plotly

dataframe = pandas.read_csv('https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv').dropna()

experienceLevelAverage = dataframe.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig = plotly.bar(experienceLevelAverage,
                x='senioridade',
                y='usd',
                title=' ',
                labels={'senioridade': 'senioridade', 'usd': 'Average Annual Salary (USD)'}
                )

fig.show()