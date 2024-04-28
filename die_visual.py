import plotly.express as px

from die import Dice

# Create a 6-sided die
die = Dice()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
poss_results =  range(1,die.num_sides+ 1 )
for value in poss_results:
    frequency_count = results.count(value)
    frequencies.append(frequency_count)

print(frequencies)

title = "Frequencies of dice roll"
labels = {"x": "die roll", "y": "frequencies"}

# Visualize the results
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
fig.show()