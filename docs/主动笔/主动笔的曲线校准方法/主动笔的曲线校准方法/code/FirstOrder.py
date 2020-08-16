import numpy as np
import math
import matplotlib.pyplot as plt

x = np.arange(0.0001, 400, 0.0001)

y = (4095 / 400) * x

plt.plot(x, y)
plt.xlabel("g")
plt.ylabel("p")
plt.xlim(0, 400)
plt.ylim(0, 4095)
plt.title("Eponential")
plt.show()
