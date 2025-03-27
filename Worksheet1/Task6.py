import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    p=math.pi
    x=np.linspace(0,2*p,1000)
    y=np.sin(x**2)
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Sin(X^2)")
    plt.show()
main()