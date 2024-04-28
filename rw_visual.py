import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk

rw = RandomWalk()
rw.fill_walk()

# Plot the point in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s = 15)
ax.set_aspect('equal')

plt.savefig("random_walk_simulation.png", bbox_inches = 'tight' )

plt.show()