import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/edgartown.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # get the high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        high = int(row[9])
        low = int(row[10])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.2)
ax.plot(dates, lows, c='blue', alpha=0.2)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.2)

# Format plot
ax.set_title("Daily high and low temps for EDG: 1/21 - present", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temp (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()