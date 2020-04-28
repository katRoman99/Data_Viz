import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Define the title and labels
plt.title("Numbers squares", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square value", fontsize=14)

# Define the size of the labels
plt.tick_params(axis='both', labelsize=14)

plt.show()