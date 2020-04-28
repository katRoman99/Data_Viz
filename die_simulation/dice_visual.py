import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

max_result = die_1.num_sides + die_2.num_sides

results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]

frequencies = [results.count(value) for value in range(2, max_result+1)]

# Results visualization
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Visualization of rolling two D8 dice 50000 times"
hist.x_labels = list(range(2, max_result+1))
hist.x_title = "Sum of the values received on two dice"
hist.y_title = "Frequency of the value received"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_simulation/dice_visual.svg')

