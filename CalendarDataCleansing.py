import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
import datetime
import numpy as np
import random



#Load Holiday Dates

idsPath     = 'C:\\Users\\Gianf\\Documents\\Data_Science\\Databases\\IndexSandbox\\USHolidayDates\\'


idsFileName = 'US_Holiday_Dates_2004_2021.csv' 
print(f'ID file located in {idsPath} . Filename:{idsFileName}') 

#Distribution of dates

ids = pd.read_csv(idsPath+idsFileName)





holidaysDistribution     = ids.groupby('Holiday').size()
yearHolidaysDistribution = ids.groupby('Year').size()




print(ids.loc[:,:])    #row,column

print(ids.loc[:,['Holiday','Year']])

print(ids.loc[((ids['Holiday']=='Western Easter') & (ids['Year']==2014)),['Holiday','Year']])
idsWestern = (ids['Holiday']=='Western Easter')




