import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0.0001, 400, 0.0001)

y = [984.63937 * math.log(a, math.e) - 1804.43185 for a in x]

plt.plot(x, y)
plt.xlabel("g")
plt.ylabel("p")
plt.xlim(0, 400)
plt.ylim(0, 4095)
plt.title("Eponential")
plt.show()
