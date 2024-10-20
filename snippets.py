import matplotlib.pyplot as plt
import numpy as np

name = ['Ram','Shyam','Rama','Kashish','Mayank']
heights = [5.1,5.5,6.0,5.0,6.3]
weights = [20,30,15,18,22]
x = np.arange(len(name))
plt.barh(name,heights,height=0.5,label='Heights',color='g')
plt.barh(x+0.5,weights,height=0.5,label='Weights',color='y')
plt.xlabel('Heights')
plt.ylabel('Names')
plt.legend()
plt.show()
