import pandas as pd
import numpy as np


# (A) Creation of DataFrame From NumPy ndarrays
a = np.array([10,20,30,40])
b = np.array([23,56,24,85])
c = np.array([-14,-41,-56,-32])
array = [a,b,c]
columns = ['A','B','C']
dframe = pd.DataFrame(array,columns)
print(dframe)

# (B) Creation of DataFrame from list of Dictionaries
listdict = [{'a':10,'b':20},{'a':32,'b':56,'c':45}]
dframelistdict = pd.DataFrame(listdict)
print(dframelistdict)


# (C) Creation of DataFrame from Dictionary of List
dictforest = {'State':['Maharashtra','Telengana','UP'],'GArea':[78438,1483,38852],'VDF':[2797,6.72,1663]}
dframe = pd.DataFrame(dictforest)
print(dframe)
print("\nTo print in our own sequence of Columns")
# To print in our own sequence of Columns
dframe = pd.DataFrame(dictforest,columns=['State','VDF','GArea'])
print(dframe)


# (D) Creation of Dataframe from Series
series1 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
series2 = pd.Series([1000,2000,-1000,-5000,1000], index= ['a','b','c','d','e'])
series3 = pd.Series([10,20,-10,-50,100], index= ['z','y','a','c','e'])

dframe = pd.DataFrame(series1)
print(dframe)

dframe = pd.DataFrame([series1,series2,series3])
print(dframe)

dframe = pd.DataFrame([series1,series3])
print(dframe)


# (E) Creation of Dataframe from Dictionary of Series
resultSheet = {'Arnab': pd.Series([90,91,97],index= ['Maths','Science','Hindi']), 
               'Ramit': pd.Series([92,81,96],index= ['Maths','Science','Hindi']), 
               'Samridhi': pd.Series([89,91,88],index= ['Maths','Science','Hindi']), 
               'Riya': pd.Series([81,61,87],index= ['Maths','Science','Hindi']), 
               'Mallika': pd.Series([94,95,99],index= ['Maths','Science','Hindi'])}
resultDF = pd.DataFrame(resultSheet)
print(resultDF)




