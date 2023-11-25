import pyodbc             
import pandas     as pd                       #IMPORT Pandas
from   sqlalchemy import create_engine    #IMPORT Sql Retriever
import datetime
import numpy as np
import random



idsPath     = 'C:\\Users\\Gianf\\Documents\\Data_Science\\Databases\\IndexSandbox\\'
idsFileName = 'IDs.xlsx' 
print(f'ID file located in {idsPath} . Filename:{idsFileName}') 

yearbase=2010
yearend=2023




ids = pd.read_excel(idsPath+idsFileName)


# testDate = datetime.date(random,random,random)


#ISSUE DATES CREATION
idsLen= len(ids)
ids['issueDate'] = np.random.randint(yearbase,yearend+1,idsLen)


# Reduce 2023 deals into previous years.
mask_2023 = ids['issueDate']==2023
len_mask_2023 = sum(mask_2023)
ids.loc[ids['issueDate']==2023,'issueDate'] = np.random.randint(yearbase,yearend+1,len_mask_2023)
distributionOfYears2 = ids.groupby('issueDate').size().reset_index()


#MATURITY DATES CREATION
minMat=1
maxMat=7

idsLen= len(ids)
ids['maturity'] = ids['issueDate']+np.random.randint(minMat,maxMat+1,idsLen)

distributionOfYears2 = ids.groupby('issueDate').size().reset_index()


#TERM
ids['term']= ids['maturity']-ids['issueDate']

#test