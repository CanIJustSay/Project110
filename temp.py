import pandas as pd
import plotly.figure_factory as pff
import random
import statistics
import os
os.system("cls")
df = pd.read_csv("data.csv")

temp = df["temp"].tolist()


finalList = []


def findOneSample():
    sampleData = []
    for i in range(1, 101):
        ranpos = random.randint(0, (len(temp)-1))
        val = temp[ranpos]
        sampleData.append(val)
    meanSD = statistics.mean(sampleData)
    finalList.append(meanSD)



for i in range(1, 1001):
    findOneSample()
meanTemp = statistics.mean(temp)
sampleMean = statistics.mean(finalList)
#print(meanTemp, sampleMean)

standardDevTemp = statistics.stdev(temp)
standardDevSample = statistics.stdev(finalList)
print(standardDevTemp,standardDevSample)
# graph = pff.create_distplot([finalList], ["Temperature"], show_hist=False)
# graph.show()

