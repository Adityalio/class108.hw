import csv
import plotly.figure_factory as ff
import pandas as pd
df = pd.read_csv("data.csv")
marks=df["Marks In Percentage"].tolist()
fig=ff.create_distplot([marks],["marks"],show_hist=False)
fig.show()