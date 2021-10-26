from os import name, stat
import random
import csv
from typing import Counter
import pandas as pd
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return(mean)

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["temperature"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "MEAN"))
    fig.show()

def setup():
    mean_list = []
    for m in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution = ",mean)
    standard_deviation= statistics.stdev(mean_list)
    print("standard deviation of sampling distribution is = ",standard_deviation)

setup()

