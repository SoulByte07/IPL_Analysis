import pandas as pd 

#load  both datasets
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")

#print the first 5 rows
print(matches.head())
print(deliveries.head())