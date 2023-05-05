import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def Zad1():
    fig = plt.figure(num=1)
    ax = fig.add_subplot(projection='3d')
    t = np.linspace(0, 2*np.pi)
    z = t
    x = np.sin(t)
    y = 2*np.cos(t)
    ax.plot(x, y, z, label='Zadanie 1')
    ax.legend()
    ax.set_xlabel('sin(z)')
    ax.set_ylabel('2*cos(z)')
    ax.set_zlabel('z')
    plt.show()

def Zad2():
    np.random.seed(19680801)
    def randrange(n, vmin, vmax):
        return (vmax-vmin)*np.random.rand(n)+vmin

    fig = plt.figure(num=2)
    ax = fig.add_subplot(111, projection='3d')

    n = 100
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5), ('g', '1', -25, 0), ('m', '.', -40, -10), ('c', 'p', -60, -40)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

def Zad3():
    fig = plt.figure(num=3, figsize=(16, 8))
    X = np.arange(-5,5,0.25)
    Y = np.arange(-5,5,0.25)
    X,Y = np.meshgrid(X,Y)
    R = np.sqrt(X **2+Y **2)
    Z = np.sin(R)
    cmaps = [cm.viridis, cm.plasma, cm.coolwarm, cm.spring, cm.bone]
    for i, cmap in enumerate(cmaps):
        ax = fig.add_subplot(2, 3, i+1, projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, antialiased=False)
        ax.set_zlim(-1.01,1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        fig.colorbar(surf,shrink=0.5,aspect=5)
        ax.set_title(cmap.name)

    plt.tight_layout()
    plt.show()

def Zad4():
    fig = plt.figure(num=4, figsize=(8, 6))
    ax1 = fig.add_subplot(221, projection='3d')
    ax2 = fig.add_subplot(222, projection='3d')
    ax3 = fig.add_subplot(223, projection='3d')
    ax4 = fig.add_subplot(224, projection='3d')

    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1

    ax1.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=0.5)
    ax1.set_title('Zacieniony z przezroczystością 0.5')

    ax2.bar3d(x, y, bottom, width, depth, top, shade=False, edgecolor='yellow')
    ax2.set_title('Nie zacieniony z krawędziami')

    ax3.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=1.0, edgecolor='black')
    ax3.set_title('Zacieniony z krawędziami')

    ax4.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=0.8, color='green', edgecolor='black')
    ax4.set_title('Zielony z krawędziami')
    plt.show()

Zad1()
Zad2()
Zad3()
Zad4()

