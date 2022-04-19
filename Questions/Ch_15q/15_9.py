from matplotlib import pyplot as plt

# Define data
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, edgecolors='none', s=40)

# Set chart title and label axes
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

plt.show()