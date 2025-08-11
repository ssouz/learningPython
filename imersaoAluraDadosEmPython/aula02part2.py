import pandas
import numpy

urlDataBase = "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"

dataframe = pandas.read_csv(urlDataBase)
print(dataframe.head)

dataframeLimpo = dataframe.dropna()
dataframeLimpo = dataframeLimpo.assign(work_year = dataframeLimpo['work_year'].astype('int64'))

print(dataframeLimpo.isnull().sum())
print(dataframeLimpo.info())
print(dataframeLimpo.head)
