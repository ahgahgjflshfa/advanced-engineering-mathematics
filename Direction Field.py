import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)

# 點點
x, y = np.meshgrid(X, Y)


# DE
dy = np.sin(x) * np.cos(y)  # 這個也是要改
dx = 1

norm = np.sqrt(dx * dx + dy * dy)
dy = dy / norm
dx = dx / norm

# plot
plt.quiver(x, y, dx, dy, color="blue")
plt.title("Direction Field")
plt.text(2, -4.8, 'CopyRight@Ping') # 這個要改
plt.show()