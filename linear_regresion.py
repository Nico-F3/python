#linear regresion

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy import stats

filename='bcna-his.csv'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 

data = pd.read_csv('bcna-his.csv', delimiter=',', header=0)
#print (data)

#print(data.columns)

df=pd.DataFrame(data).to_numpy()#con esto creo un array en numpy/panda que puedo manipular

#print(data)

df=np.delete(df, slice(0,4),1)#eliminate the columns from 0 to 4 in a numpy array
df=np.delete(df, slice(0,4),0)#eliminate the arrows from 0 to 4 in a numpy array


xarr=df[:,2]

yarr=df[:,0]

x=[]
y=[]
for i in df[:,2]:
    x.append(i)
for j in df[:,0]:
    y.append(j)



slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)#calculates all the values
# base on the 'x' and 'y' provided by me

plt.plot(xarr, intercept + slope * xarr, '-',color='red',label='{}+\n{}X'.format(intercept,slope))
plt.scatter(x=xarr,y=yarr,)

plt.legend(loc="upper left")
plt.title('standard concentration')
plt.xlabel('concentration ug/ml')
plt.ylabel('Abs at 595')
plt.grid(True)
plt.savefig("linear regresion.png")

#print(xarr,'\n',yarr,'\n',r_value**2)