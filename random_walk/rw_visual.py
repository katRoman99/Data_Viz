import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Prepare the data for random walk
rw = RandomWalk(50000)
while True:
    rw.reset_walk()
    rw.fill_walk()

    # Define the size of the window
    plt.figure(figsize=(10, 6))

    # Style the plot
    point_numbers = list(range(rw.num_points))


    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges, edgecolor='none', s=3)

    #plt.plot(rw.x_values, rw.y_values, linewidth=2)

    # Fill in starting and ending points in different colours
    plt.scatter(rw.x_values[0], rw.y_values[0], c='yellow', s=5)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=5)

    # Hide both axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    plt.show()

    keep_running = input("Do you want to create another random walk? (y/n): ")
    if keep_running == 'n':
        break