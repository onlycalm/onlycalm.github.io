import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0, 12, 0.0001)

#基带信号
y1 = []
for v in x:
    if v < 4:
        y1.append(0)
    elif v < 8:
        y1.append(1)
    elif v < 12:
        y1.append(0)

#载波信号
y2 = []
m = 1                   #PWM起始电平高
u = 1
for v in x:
    if v < u:
        pass
    else:
        u += 1
        if m == 1:
            m = 0
        else:
            m = 1

    y2.append(m)

#BPSK调相信号
y3 = []
for v in x:
    n = int(v * 10000)
    if y1[n] == 1:
        if y2[n] == 1:
            y3.append(0)
        elif y2[n] == 0:
            y3.append(1)
    elif y1[n] == 0:
        y3.append(y2[n])

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
