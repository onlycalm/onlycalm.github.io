import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.0001)

#基带信号
y1 = []
for v in x:
    if v < 1:
        y1.append(1)
    elif v < 2:
        y1.append(0)
    elif v < 4:
        y1.append(1)
    elif v < 6:
        y1.append(0)

#载波信号
y2 = np.sin(2 * math.pi * (x - 1 / 2))

#BPSK调相信号
y3 = []
for v in x:
    n = int(v * 10000)
    if y1[n] == 1:
        y3.append(y2[n])
    elif y1[n] == 0:
        y3.append(-y2[n])

#设置窗格大小
Window = plt.figure(num = 3)
#添加子图
Line1 = Window.add_subplot(3, 1, 1)
Line2 = Window.add_subplot(3, 1, 2)
Line3 = Window.add_subplot(3, 1, 3)

Line1.plot(x, y1)
Line2.plot(x, y2)
Line3.plot(x, y3)

plt.show()
