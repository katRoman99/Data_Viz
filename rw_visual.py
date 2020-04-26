import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare the data for random walk
rw = RandomWalk()
while True:
    rw.reset_walk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Do you want to create another random walk? (y/n): ")
    if keep_running == 'n':
        break