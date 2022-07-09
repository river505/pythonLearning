
from matplotlib import pyplot as plt
import random
import matplotlib


matplotlib.rc("font", family= 'Microsoft YaHei', weight= 'bold')

plt.figure(figsize=(20, 8), dpi=80)
x = range(0, 120)
a = [random.randint(25, 30) for i in range(120)]
xlabel = ["10点{}分".format(i) for i in range(60)]
xlabel += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], xlabel[::3], rotation=45)
plt.plot(x, a)
plt.show()
