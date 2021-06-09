import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("C:\\Users\\Dhairya\\Desktop\\python\\c 108\\project\\c 108 project\\data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=True)
fig.show()
print("Opening")