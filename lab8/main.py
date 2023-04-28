import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zad1
x = np.arange(1, 21)
y = 1/x
plt.plot(x, y, label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.legend()
plt.axis([1, 20, 0, 1])
plt.grid(True)
plt.show()

#Zad2
x = np.arange(1, 21, 1)
y = 1/x
plt.plot(x, y, 'g-->', label="f(x)=1/x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x [1,20]")
plt.legend()
plt.axis([0, 20, 0, 1])
plt.grid(True)
plt.show()

#Zad3
x = np.arange(0, 30.1, 0.1)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres sin(x), cos(x)")
plt.legend()
plt.axis([-0.5, 31.5, -1.1, 1.1])
plt.show()

#Zad4
x = np.arange(0, 30.1, 0.1)
y = np.sin(x) + 2
z = -np.sin(x)
plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc=1)
plt.axis([-0.5, 31.5, -1.1, 3.1])
plt.show()

#Zad5
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
ds = pd.read_csv(url, names=names)
data = ds.iloc[:, :-1].values
x = data[:,0]
y = data[:,1]
size = np.abs(x - y)
color = np.random.randint(0, 50, len(x))
plt.scatter(x, y, c=color, s=size)
plt.colorbar()
plt.show()