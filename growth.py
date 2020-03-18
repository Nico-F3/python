import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics


filename='growht.csv'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile) 


data = pd.read_csv('growht.csv', delimiter=',', header=0)

x=[]

for l in data['Time']:
    x.append(l)

data = data.drop(columns="Blank")#eliminate the column wich name in '' in this case the Blank column
data = data.drop(columns="Time")



y=[]
i=2
dict = data.to_dict(orient='list')

for values in dict.values():
    y.append(values)


yarr=np.array([np.array(yi) for yi in y])

yavg=[]
i=2
while i <len(y):
    result = [statistics.mean(k) for k in zip(y[i-2],y[i-1],y[i])]
    yavg.append(result)
    i=i+3


sd=[]
h=2  
while h <len(y):
    error = [statistics.stdev(k) for k in zip(y[h-2],y[h-1],y[h])]
    sd.append(error)
    h=h+3
print(sd)
#error = [statistics.stdev(k) for k in zip(y[0],y[1],y[2])]

print(data.columns[0])

j=0
for i in range(len(yavg)):
    #print(yavg[i])
    plt.scatter(x=x,y=yavg[i], label=data.columns[j])
    #plt.plot(x,yavg[i])
    plt.errorbar(x, yavg[i], sd[i],capsize=3)#plt.errorbar accepts the same arguments as plt.plot with additional yerr and xerr which default to None (i.e. if you leave them blank it will act as plt.plot).
    plt.legend(loc="upper left")
    plt.title('growth curve')
    plt.xlabel('time (days)')
    plt.ylabel('OD550')
    plt.grid(True)
    j=j+3
plt.savefig("growthcurve.png")