
import plotly.figure_factory as ff
import pandas as pd

df=pd.read_csv('D:\project\class108\data.csv')

AvgRating=df['Avg Rating'].tolist()
fig=ff.create_distplot([AvgRating],['Average distribution of company '],show_hist=True)
fig.show()