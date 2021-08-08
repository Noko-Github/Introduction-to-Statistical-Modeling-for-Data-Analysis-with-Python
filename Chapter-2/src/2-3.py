import math

import numpy as np
import matplotlib.pyplot as plt

def poisson(_lambda, k):
    k = int(k)
    prob = (_lambda ** k) * (math.exp(-1 * _lambda)) / math.factorial(k)
    
    return prob


# 1.平均(λ)が3.56のポアソン分布の描画
x = np.arange(0, 10, 1)
y = [poisson(3.56, k) for k in x]

plt.plot(x, y, linewidth=2, color="blue", linestyle="dashed", marker="o")
plt.show()


# 1.様々な平均(λ)のポアソン分布の描画
x = np.arange(0, 21, 1)
lambda_list = [3.5, 7.7, 15.1]
color_list = ["red", "blue", "green"]

for _lambda, color in zip(lambda_list, color_list):
    y = [poisson(_lambda, k) for k in x]
    plt.plot(x, y, linewidth=2, color=color, linestyle="dashed", marker="o")

plt.show()