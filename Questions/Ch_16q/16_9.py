# 16-9. World Fires: In the resources for this chapter, you’ll find a file called world_fires_1_day.csv. 
# This file contains information about fires burning in different locations around the globe, including the latitude and longitude, and the brightness of each fire. 
# Using the data processing work from the first part of this chapter and the mapping work from this section, 
# make a map that shows which parts of the world are affected by fires. You can download more recent versions of this data at 
# https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data/. You can find links to the data in CSV format in the TXT section.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 358). No Starch Press. Kindle Edition. 

import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

num_rows = 10000

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get brightness, lats and lons, and dates.
    dates, brightnesses = [], []
    lats, lons = [], []
    hover_texts = []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        label = f"{datetime.strftime('%m/%d/%y')} - {brightness}"
        
        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])
        hover_texts.append(label)
        
        row_num += 1
        if row_num == num_rows:
            break

# Map the fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [brightness/20 for brightness in brightnesses],
        'color': brightnesses,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]

my_layout = Layout(title='Global Fire Activity')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')