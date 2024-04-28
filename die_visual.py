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

# Rolling 2 dice
dice_one = Dice()
dice_two = Dice()

results = []
for roll_num in range(1000):
    result = dice_one.roll() + dice_two.roll()
    results.append(result)

frequencies = []
max_result = dice_one.num_sides + dice_two.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling two dice"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
# Further customize the graph
fig.update_layout(xaxis_dtick=1)
fig.show()


dice_one = Dice()
dice_two = Dice(10)

results = []
for roll_num in range(50_000):
    result = dice_one.roll() + dice_two.roll()
    results.append(result)

frequencies = []
max_result = dice_one.num_sides + dice_two.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling two dice"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = labels)
# Further customize the graph
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html('dice_visual_d6d10.html')

