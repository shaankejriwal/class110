import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)

population_sd = statistics.stdev(data)

print("population mean is = ",population_mean)
print("population standard deviation is = ",population_sd)

# data = ff.create_distplot([data],["temp"],show_hist = False)
# data.show()