import numpy as np
import matplotlib.pyplot as plt
def f ( x ) :
    y = np.tan(x) - x - 1
    return y

def main( ):
    x = np.linspace ( 0, 2 * np.pi, 100 ) # 這個要改
    y = f ( x )
    plt.plot ( x, y )
    plt.xlabel ( 'x' )
    plt.ylabel ( 'f(x)' )
    plt.title ( 'Plot of the Function f(x) = tanx - x - 1' ) # 這隨緣
    plt.xlim(0, 4 * np.pi)  # 這個也是要改
    plt.text ( 4, 0, 'Copyright@Chou' ) # 請加上你的數位簽章 這個也要改
    plt.show ()

main( )
