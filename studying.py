import pandas as pd
import plotly.figure_factory as pff
import statistics
import random
import os
os.system("cls")

df = pd.read_csv("medium_data.csv")

time = df["reading_time"].tolist()



finalList = []
def Sample():
    sampleData = []
    for i in range(1,101):
        ranpos = random.randint(0, (len(time)-1))
        val = time[ranpos]
        sampleData.append(val)
    mean = statistics.mean(sampleData)
    finalList.append(mean)


for i in range(1, 1001):
    Sample()
graph = pff.create_distplot([finalList], ["Reading Time"], show_hist=False)
graph.show()