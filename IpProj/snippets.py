import pandas as pd
import matplotlib.pyplot as plt
stock = pd.read_csv('D:/Coding/Python//school/IpProj/IpProj.csv')

print(stock)
try:
    print(stock.loc[stock['TAmt'] == stock.TAmt.max(),'IndexNo','Name'])
except(pd.errors.IndexingError):
    print('Error Occured')
