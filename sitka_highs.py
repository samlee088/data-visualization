from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract dates and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

print(highs)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
ax.plot(dates, highs, color = 'red')
ax.plot(dates, lows, color = 'blue')

# Format plot
ax.set_title("Daily high temperatures, July 2021", fontsize = 24)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (f)", fontsize = 16)
ax.tick_params(labelsize = 16)

plt.show()

