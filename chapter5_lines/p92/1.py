from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

# 创建画布和 3D 坐标系（修改关键点）
fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # 使用 add_subplot 替代 gca

# 生成数据
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 绘制 3D 曲面
surf = ax.plot_surface(
    X, Y, Z,
    rstride=1,
    cstride=1,
    cmap=cm.coolwarm,
    linewidth=0,
    antialiased=False
)

# 设置坐标轴范围
ax.set_zlim(-1.01, 1.01)

# 配置 Z 轴刻度
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# 添加颜色条
fig.colorbar(surf, shrink=0.5, aspect=5)

# 显示图形
plt.show()