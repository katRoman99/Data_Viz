import pygal

from die import Die

die = Die()

results = []

for roll_num in range(1000):
    roll_num = die.roll()
    results.append(roll_num)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Results visualization
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Visualization of a die roll 1000 times"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Value on the die"
hist.y_title = "Frequency of the value received"

hist.add('D6', frequencies)
hist.render_to_file('die_simulation/die_visual.svg')


