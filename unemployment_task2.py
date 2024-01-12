
######### WAP TO LERN MACHINE TO PLOT THE UNEMPLOYMENT RATE  #######

import numpy as np  #linear algebra 
import pandas as pd  #data processing 

df=pd.read_csv("Unemployment_in_indiatask2.csv") #read dataset

df.head() #returns first 5 entries

df.tail() #returns last 5 entries

#returns tuple of shape (Rows, columns) of dataframe
df.shape 

#prints information about the dataframe
df.info()

#returns numerical description of the data in the dataframe
df.describe()

x = df['Region'] #plotting column 'Region' on x-axis
x #print x

y=df[' Estimated Unemployment Rate (%)'] #plotting column 'Estimated Unemployment Rate (%)' on y-axis

y #print y

df2=df.iloc[:,3]

df2

import plotly.express as px
import matplotlib.pyplot as plt

fg = px.bar(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (State Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


fg = px.bar(df,x='Region.1',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (Region Wise) by Bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


fg = px.box(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
            title='Unemploymeny Rate (Statewise) by Box Plot',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


fg = px.scatter(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
                title='Unemploymeny Rate (Statewise) by Scatter Plot',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg = px.histogram(df,x='Region',y=' Estimated Unemployment Rate (%)',color='Region',
                  title='Unemploymeny Rate (Statewise) by Histogram',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()
