import numpy as np
from sympy import *
import matplotlib.pyplot as plt

alpha = 0.1

# Gradient:
#   Xn+1 = Xn - alpha * f'(Xn)

GradientX = [0] # 用來儲存 X0 到 X10 的值

x = Symbol('x')
gradientFunc = x - alpha * diff(x ** 2 - 2 * x + 3, x) 

for n in range(10):
    next = float(gradientFunc.evalf(subs={'x': GradientX[n]}))    # 計算 Xn+1(next)

    #print(next)

    GradientX.append(np.round(next, 3)) # 塞進陣列最後

# Newton:
#   Xn+1 = Xn - f(Xn) / f'(Xn)

NewtonX = [0]

newtonFunc = x - (x ** 2 - 2 * x + 3) / diff(x ** 2 - 2 * x + 3, x)

for n in range(10):
    next = float(newtonFunc.evalf(subs={'x': NewtonX[n]}))

    NewtonX.append(np.round(next, 3))

plt.title("Gradient and Newton Method")

plt.plot([i for i in range(11)], GradientX, color="blue", label="Gradient Method") # 顯示Gradient Method 計算出的曲線

plt.plot([i for i in range(11)], NewtonX, color="red", label="Newton Method")

plt.xlim(-0.5, 1.5)

plt.text(-0.5, -1, 'CopyRight@Chou') # 這個也要改

plt.legend()

plt.show()