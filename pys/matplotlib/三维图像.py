import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

X=[1,1,2,2]
Y=[2,4,4,3]
z=[8,2,3,4]
fig=plt.figure()
ax=Axes3D(fig)
ax.plot_trisurf(X, Y, z)
plt.show()