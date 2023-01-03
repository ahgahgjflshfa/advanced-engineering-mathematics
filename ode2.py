import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

X = np.linspace ( -2 , 2 , 100 ) # 這裡也要 I
Y = np.linspace ( -2, 2 , 100 ) # 這裡要改 I
x, y = np.meshgrid ( X, Y ) # 產生網狀格點
z = np.log(np.abs(np.sin(x))) + 2 * np.log(np.abs(y)) + y # 改成算出來的 f(x,y)

# 3D Plot (Surface Plot)
fig = plt.figure (1)
ax = fig.add_subplot(projection='3d')
ax.plot_surface ( x, y, z, cmap = cm.coolwarm, linewidth = 0, antialiased = False )
plt.xlabel ( 'x' )
plt.ylabel ( 'y' )
plt.title ( '3D Plot of f(x,y)' )
plt.show()
