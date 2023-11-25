import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
from datetime import datetime
import numpy as np
import random
import time                              #Check Running times

insert = 1


#Database Connection Parameters
server = 'DESKTOP-J9GGR42'  # e.g., 'localhost\sqlexpress'
database = 'indexSandbox'
driver = 'ODBC Driver 17 for SQL Server'  # May vary based on your installed ODBC driver
# Connection URL
conn_url = f'mssql+pyodbc://{server}/{database}?driver={driver}&trusted_connection=yes'
#SQL Engine
engine = create_engine(conn_url)




filePath     = 'C:\\Users\\Gianf\\Documents\\Data_Science\\Databases\\IndexSandbox\\DummyDataSet\\'
fileName = 'dummy_bonds_dataset.csv' 

print(f'ID file located in {filePath} . Filename:{fileName}') 


table = 'bondsinstruments'

fileDf=pd.read_csv(filePath+fileName)

fileDf = fileDf.rename(columns={
    'Bond Name':'bondID',
    'ISIN':'ISIN',
    'Issuer':'Issuer',
    'Issue Date':'IssueDate',
    'Maturity Date':'MaturityDate',
    'Coupon Rate':'CouponRate',
    'Face Value':'FaceValue',
    'Market Value':'MarketValue',
    'Currency':'Currency',
    "Moody's Rating":'MoodysRating',
    'S&P Rating':'SPRating',
    'Fitch Rating':'FitchRating',
    'Sector':'Sector',
    'Reference Rate':'ReferenceRate',
    'Seniority':'Seniority',
    'Type of Bond':'TypeOfBond'
})




# Insert DataFrame into SQL Server
if insert ==1:
    fileDf.to_sql(table, con=engine, if_exists='append', index=False)


print(fileDf)







