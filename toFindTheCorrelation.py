import plotly.express as px
import csv
import numpy as np
import pandas as pd

def plot(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig  =  px.line(df, x="Roll No",y="Marks In Percentage",title="Marks of the students")
        fig.show()

def getDataSource(data_path):
    size = []
    time = []

    with open(data_path) as f:
        df = csv.DictReader(f)

        for row in df:
            size.append(float(row['Roll No']))
            time.append(float(row['Marks In Percentage']))

    return {"x": size,"y": time}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('The correlation between the roll no and marks is ' + str(correlation[0,1]))

def setup():
    data_path = './marks.csv'
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plot(data_path)

setup()
