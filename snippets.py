import numpy as np
import pandas as pd
dict = [1,2,3,4,5,6,7]
index = ['A','B','C','D','E','F','G']
series = pd.Series(dict, index=index)
series.name = 'Numbers'
series.index.name = 'Aplha'
print(series)
print(series.values)
print(series.size)
print(series.empty)
