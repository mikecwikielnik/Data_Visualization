import csv
from turtle import color
from matplotlib import pyplot as plt
from plotly.graph_objs import Bar, Layout
from plotly import offline
from plotly import colors

filename = 'iihs_data.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    cars, avgloss = [], []
    for row in reader:
            car = row[0]
            avglos = float(row[1])
            cars.append(car)
            avgloss.append(avglos)
            
       
plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.scatter(cars, avgloss)
x_axis_config = {'title': 'Cars', 'dtick': 1}
y_axis_config = {'title': 'Average loss', 'dtick': 50}
my_layout = Layout(title = 'Practice graph', 
                   xaxis = x_axis_config, yaxis = y_axis_config)
offline.plot({'layout': my_layout}, filename='practicegraph.html')
plt.show()

# plt.title("Titletown", fontsize = 25)
# plt.xlabel("cars", fontsize = 16)
# plt.ylabel("average loss", fontsize = 16)
# plt.show()
           

# data = [Bar(x=cars, y=avgloss, color = 'size')]

# x_axis_config = {'title': 'Cars', 'dtick':1}
# y_axis_config = {'title': 'Average Loss'}
# my_layout = Layout(title='Practice graph',
#                    xaxis=x_axis_config, yaxis=y_axis_config,)
# offline.plot({'data': data, 'layout': my_layout}, filename='practicegraph.html')
# plt.show()