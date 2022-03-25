import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
    x = df.groupby("level")["attempt"].mean(),
    y = ['Level1','Level2','Level3','Level4'],
    
))

fig.show()