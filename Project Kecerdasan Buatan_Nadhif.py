
import pandas as pd
import seaborn as sns 
pd.set_option("display.max_columns",None) 
pd.set_option("display.max_rows",None) 
import warnings
warnings.filterwarnings("ignore")
sns.set(style="darkgrid", palette="pastel", color_codes=True)
sns.set_context("paper")

#Plotly imports
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "seaborn"

#Import CSV File
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


buttons = []
i = 0
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



    
fig3.update_layout  (updatemenus=[
                                dict(active=0,
                                    type="dropdown",
                                    buttons=buttons,
                                    x = 0.045,
                                    y = 1.075,
                                    xanchor = 'left',
                                    yanchor = 'top')
                                ]
                        )
fig3.update_layout(
    annotations=[
    dict(text="Usia", x=0, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False )])

fig3.update_layout(
    xaxis_title="Product Treadmill",
    yaxis_title="Income CardioGood Fitness",
    autosize=False,
    width=1000,
    height=800,)

fig3.show()