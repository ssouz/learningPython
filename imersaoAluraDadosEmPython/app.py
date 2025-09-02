from email.policy import default
from os import write

import seaborn
import streamlit
import plotly.express as plotly
import pandas
from matplotlib.style.core import available

urlSalarios = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"
dataframe = pandas.read_csv(urlSalarios)

streamlit.sidebar.header("filtros" )

#ano
availableYears = sorted(dataframe["ano"].unique())
selectedYears = streamlit.sidebar.multiselect("ano", availableYears,default=availableYears)

#senioridade
experienceLevelAvailable = sorted(dataframe["senioridade"].unique())
experienceLevelSelected = streamlit.sidebar.multiselect("senioridade",experienceLevelAvailable, default=experienceLevelAvailable)

#tipo de contrato
contractTypeAvailale = sorted(dataframe["contrato"].unique())
contractTypeSelect = streamlit.sidebar.multiselect("contrato", contractTypeAvailale, default=contractTypeAvailale)


#tamanho da empresa
company_sizeAvailable = sorted(dataframe["tamanho_empresa"].unique())
company_sizeSelect = streamlit.sidebar.multiselect("tamanho_empresa", company_sizeAvailable, default=company_sizeAvailable)

filteredDataframe = dataframe[
    (dataframe['ano'].isin(availableYears)) &
    (dataframe['senioridade']) &
    (dataframe['contrato'])&
    (dataframe['tamanho_empresa'])
]
#conteudo principal
streamlit.title("Dashboard salario área de dados")
streamlit.markdown(
    """
    Este dashboard apresenta uma análise dos salários na área de dados no Brasil.
    Utilize os filtros na barra lateral para explorar os dados por ano, senioridade, tipo de contrato e tamanho da empresa.
    Os dados são provenientes do repositório público do GitHub.
    """
)
streamlit.write(seaborn.barplot(data=filteredDataframe, x='experience_level',y='salary_in_usd')
)

streamlit.set_page_config(
    page_title="dashboard salario na area de dados",
    page_icon="",
    layout="wide",


)
