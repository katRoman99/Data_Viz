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

print(frequencies)
