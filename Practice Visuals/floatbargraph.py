"""
Practice graph
"""

import csv
from turtle import color
from plotly.graph_objs import Bar, Layout
from plotly import offline


filename = 'iihs_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get the names of the cars from this file
    cars, avgloss = [], []
    for row in reader:
        try:
            car = row[0]
            avglos = float(row[1])
        except NameError:
            print("error")
        else:
            cars.append(car)
            avgloss.append(avglos)

data = [Bar(x=cars, y=avgloss)]

x_axis_config = {'title': 'Cars'}
y_axis_config = {'title': 'Average Loss'}
my_layout = Layout(title='Practice graph',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='practicegraph.html')