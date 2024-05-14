import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = np.arange(11, 21)

plt.scatter(x, y, marker="*", c='g', alpha=0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.show()
