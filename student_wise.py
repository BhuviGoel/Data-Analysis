import pandas as pd
import csv
import plotly.graph_objects as bo

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Class 107 - Data Analysis\data.csv")
student_data = data.loc[data['student_id'] == "TRL_abc"]

mean_std = student_data.groupby("level")["attempt"].mean()
fig = bo.Figure(bo.Bar(x = ["Level 1","Level 2","Level 3","Level 4"], y =mean_std , orientation = 'v' ))
fig.show()