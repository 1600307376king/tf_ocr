import cv2
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D
from matplotlib import cm
import matplotlib.animation as animation

image = cv2.imread('./in.png', 0)
# print(image)
# print(np.shape(image))

# 设置matplotlib正常显示中文和负号
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
#
# plt.hist(image.flatten(), bins=255, facecolor='blue', edgecolor='black')
#
# plt.xlabel("区间")
# plt.ylabel("频率")
# plt.title("灰度值分布直方图")
# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#
# x = [[1, 1, 2, 2],
#      [3, 4, 4, 3],
#      [1, 2, 1, 1]]
#
# ax.plot_trisurf(x[0], x[1], x[2])
# plt.show()

position_list = [[], [], []]
for k, v in enumerate(image):
    for j, v2 in enumerate(v):
        position_list[0].append(k)
        position_list[1].append(j)
        position_list[2].append(v2)


print(position_list)
# print(np.shape(position_list))
ax.plot_trisurf(position_list[0], position_list[1], position_list[2], cmap=cm.coolwarm)
ax.view_init(elev=90, azim=0)
plt.show()