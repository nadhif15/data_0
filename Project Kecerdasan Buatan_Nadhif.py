from itertools import product
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
pd.set_option("display.max_columns",None) 
pd.set_option("display.max_rows",None) 
import warnings
warnings.filterwarnings("ignore")
from IPython.display import Image
sns.set(style="darkgrid", palette="pastel", color_codes=True)
sns.set_context("paper")
from datetime import datetime
import datapane as dp

#Plotly imports
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "seaborn"
from plotly.subplots import make_subplots


df = pd.read_csv('CardioGoodFitness.csv')

df.head()

#Renaming the coulmns for easy usage
df.rename(columns={'Product': 'product', 
                     'Age':'age',
                     'Education':'education',
                     'Gender':'gender',
                     'MaritalStatus':'maritalstatus', 'Usage':'usage',
                     'Fitness': 'fitness',
                     'Income':'income',
                     'Miles':'miles'
                    }, inplace=True)

# Active Case = confirmed - deaths - recovered


buttons = []
buttonss =[]
i = 0
j = 0
fig3 = go.Figure()

age_list = list(df['age'].unique())
gender_list = list(df['gender'].unique())

for age in age_list:
    fig3.add_trace(
        go.Scatter(
            x = df['product'][df['age']==age],
            y = df['income'][df['age']==age],
            name = int(age), visible = (i==0)
        )
    )
for gender in gender_list:
    fig3.add_trace(
        go.Scatter(
            x = df['product'][df['gender']==gender],
            y = df['income'][df['gender']==gender],
            name = gender, visible = (j==0)
        )
    )


    
for age in age_list:
    args = [False] * len(age_list)
    args[i] = True
    
    #create a button object for the gender we are on
    button = dict(label = int(age),
                  method = "update",
                  args=[{"visible": args}])
    
    #add the button to our list of buttons
    buttons.append(button)
    
    #i is an iterable used to tell our "args" list which value to set to True
    i+=1


for gender in gender_list:
    args = [False] * len(gender_list)
    args[j] = True
    
    #create a button object for the gender we are on
    button = dict(label = gender,
                  method = "update",
                  args=[{"visible": args}])
    
    #add the button to our list of buttons
    buttonss.append(button)
    
    #i is an iterable used to tell our "args" list which value to set to True
    j+=1

    
fig3.update_layout  (updatemenus=[
                                dict(active=0,
                                    type="dropdown",
                                    buttons=buttons,
                                    x = 0.045,
                                    y = 1.075,
                                    xanchor = 'left',
                                    yanchor = 'top'),
                              
                                dict(active=1,
                                    type="dropdown",
                                    buttons=buttonss,
                                    x = 0.195,
                                    y = 1.075,
                                    xanchor = 'left',
                                    yanchor = 'top'),
                                ]
                        )
fig3.update_layout(
    annotations=[
        dict(text="Usia", x=0, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False, ),
        dict(text="Gender", x=0.125, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False)])

fig3.update_layout(
    xaxis_title="Product Treadmill",
    yaxis_title="Income CardioGood Fitness",
    autosize=False,
    width=1000,
    height=800,)

fig3.show()