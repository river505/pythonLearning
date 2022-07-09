from matplotlib import pyplot as plt
fig=plt.figure(figsize=(20, 8), dpi=80)
x = range(2, 26, 2)
y = [2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4]
plt.plot(x, y)
asd=x[::3]
plt.xticks(asd)

plt.savefig(".\img\p1.svg")
plt.show()
