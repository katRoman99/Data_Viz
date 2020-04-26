import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Color mapping and points scattering
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues , edgecolor='none', s=40)

# Define title and labels
plt.title("Squares of numbers", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square values", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

# Define the scope for each of the axis
plt.axis([0, 1100, 0, 1100000])

plt.show()