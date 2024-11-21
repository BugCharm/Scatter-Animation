import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

num = 100
x,y =  np.random.rand(2, num) * 10
colors = np.random.rand(num)
sizes = np.random.rand(num ) * 1000

fig, ax = plt.subplots()
scat = ax.scatter(x, y, c=colors, s= sizes)
ax.set_xlim(0,10)
ax.set_ylim(0,10)

def animate(i):
    scat.set_offsets(
        np.c_[x + 
              np.random.randn(num) * 0.1, 
              y + np.random.rand(num) * 0.1])
    return scat,


ani = animation.FuncAnimation(fig, animate,
                              frames = 100,
                              interval = 50)
ani.save('scatter.gif', writer='pillow')
plt.show()