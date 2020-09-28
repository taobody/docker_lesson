import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 100, 0.5)

Hz = 5.
y = np.sin(2.0 * np.py * (x * Hz) / 100)

plt.plot(x, y)
plt.savefile('test.png')