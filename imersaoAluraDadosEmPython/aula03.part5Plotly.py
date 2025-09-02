import pandas
import plotly.express as px

dataframe = pandas.read_csv('https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv').dropna()

remote_count = dataframe['remoto'].value_counts().reset_index()
remote_count.columns = ['Tipo de Trabalho', 'Quantidade']

fig = px.pie(
    remote_count,
    names='Tipo de Trabalho',
    values='Quantidade',
    title='Distribuição de Trabalho Remoto',
    color_discrete_sequence=px.colors.sequential.RdBu,
    hole=0.4
)

fig.update_traces(
    textinfo='percent+label',
    pull=[0.05]*len(remote_count)
)
fig.update_layout(
    legend_title_text='Tipo de Trabalho',
    legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5)
)

fig.show()
