import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the point in the walk.
plt.style.use('classic')
# fig, ax = plt.subplots()
# Adjustment to rendering plot with different window sizes, ie different screen resolution
fig, ax = plt.subplots(figsize=(10,6), dpi = 128)
ax.scatter(rw.x_values, rw.y_values, s = 15)
ax.set_aspect('equal')

plt.savefig("random_walk_simulation.png", bbox_inches = 'tight' )

plt.show()

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk
    rw = RandomWalk(1_000_000)
    rw.fill_walk()

    # Plot the point in the walk.
    plt.style.use('classic')
    # fig, ax = plt.subplots()
    # Adjustment to rendering plot with different window sizes, ie different screen resolution
    fig, ax = plt.subplots(figsize=(10,6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 1)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    ax.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig("random_walk_simulation.png", bbox_inches = 'tight' )

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
