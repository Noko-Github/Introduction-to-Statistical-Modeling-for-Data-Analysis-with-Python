import math

import numpy as np
import matplotlib.pyplot as plt
import rdata

from util import poisson

parsed = rdata.parser.parse_file('../../kubobook_2012/distribution/data.RData')
data = rdata.conversion.convert(parsed)['data'].astype('int8')

x = np.arange(0, 9, 1)

# 対数尤度とヒストグラムを重ねたグラフを表示
fig = plt.figure()
lambda_list = np.arange(2, 5.6, 0.4)
for idx, _lambda in enumerate(lambda_list, 1):
    
    # ポアソン分布から確率を各事象が発生する確率を算出
    y = [poisson(_lambda, k) for k in x]
    ax1 = fig.add_subplot(3, 3, idx)
    ax1.plot(x, y)

    ax2 = ax1.twinx()
    ax2.hist(data, bins=8)

    # ポアソン分布の対数尤度を算出
    log_l = 0
    for value in data:
        k = sum([math.log(i) for i in range(1, value+1, 1)])
        log_l += value * math.log(_lambda) - _lambda - k

    ax2.text(5, 10, f'lambda={_lambda}')
    ax2.text(5, 9, f'log_L={log_l}')

plt.show()


# lambdaを変化させた時の対数尤度の変化を表示
x = np.arange(2, 5, 0.1) 
y = []
for _lambda in x:

    # ポアソン分布の対数尤度を算出
    log_l = 0
    for value in data:
        k = sum([math.log(i) for i in range(1, value+1, 1)])
        log_l += value * math.log(_lambda) - _lambda - k
    y += [log_l]

plt.plot(x, y)    
plt.axvline(x[np.argmax(y)], linestyle='--', color='red')
plt.show()


