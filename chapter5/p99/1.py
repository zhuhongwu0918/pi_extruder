import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,5,0.1)
print(x)
y= np.sin(x)
plt.plot(x,y)
plt.show()      #加上这一个方法才能显示