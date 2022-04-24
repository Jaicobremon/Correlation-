# Importing modules
import numpy as np
import pandas as pd
import csv
import plotly.express as px

#Reading csv file
df = pd.read_csv("StudentMarksDays.csv")

#Defining function to get data from csv file and how to get the data
def getDataSource(data_path):
    daysPresent = []
    marks = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            daysPresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return{"x":daysPresent,"y":marks}

# Function getting correlation from data
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])

    print("The correlation between the days present in class and the marks in percentage is --> ",correlation)

#Specifying where is the data
data_path = "StudentMarksDays.csv"
dataSource = getDataSource(data_path)

#Calling function
findCorrelation(dataSource)

#Creating scatterplot to show data
chart = px.scatter(df, x = "Days Present", y = "Marks In Percentage")

#Showing chart
chart.show()