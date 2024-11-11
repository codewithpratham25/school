import pandas as pd
import matplotlib.pyplot as plt
stock = pd.read_csv('D:/Coding/Python//school/IpProj/IpProj.csv')

company = str(input('ENTER THE COMPANY NAME: '))
print(stock[['IndexNo','Qty','Name']][(stock['Company'] == company)])
