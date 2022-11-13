import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Importing the table with the data
data = pd.read_csv('/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_1/table_.csv')

#Selecting which information will be analyzed
select = [data['happyScore'],data['GDP']]

#Naming the 'x' and 'y' axes
plt.xlabel('GDP(per capita )')
plt.ylabel('Happy Score')
plt.title("Analyzing country characteristics", 
          fontdict={'family': 'monospace', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 16},
          loc='center')

#Sorting values from smallest to largest (top to bottom)
data.sort_values('GDP', inplace=True)

#Filtering which country has the highest GDP per capita and the lowest GDP per capita.
richest=data[data['GDP']==(np.max(data['GDP']))]
for k,row in richest.iterrows():
    plt.text(row['GDP'],row['happyScore'],row['country']) 
    
poorer=data[data['GDP']==(np.min(data['GDP']))]
for k,row in poorer.iterrows():
    plt.text(row['GDP'],row['happyScore'],row['country'])    

plt.scatter(select[1],select[0])

