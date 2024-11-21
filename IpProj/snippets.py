import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy

engine = sqlalchemy.create_engine(f'mysql+pymysql://root:mysql@localhost:3306/invmanagement')
userDf = pd.read_sql_query('SELECT * FROM userandpass',engine)
print(userDf)
passw = ['prath@123']
passDict = {'Username':pd.Series(passw)}
passdf = pd.DataFrame(passDict)
print(passdf)
hel = (passdf == userDf[['Username']][(userDf['Password'] == passw)])
cond = (hel.all())
if cond.values == False:
    print('Hel')

# print(passdf == userDf[['Username']][(userDf['Password'] == passw)])
