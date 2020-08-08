import numpy as np
import matplotlib.pyplot as plt

rand = (np.random.random(2)-0.5)*30
rand1 = (np.random.random(2)-0.5)*30
rand2 = (np.random.random(2)-0.5)*30


def generate(x,y):
    result = np.sin(-0.3*x+0.1*y)*(x-rand[0])**2 + np.sin(0.03*x-0.2*y)*(y-rand[1])**2 + np.sin(0.1*x+0.015*y)*(x-rand1[0])**2 + (y-rand1[1])**2 + 4*(x-rand2[0])**2 + (y-rand2[1])**2
    return result



x = np.arange(-20,20,0.1)
X,Y = np.meshgrid(x,x)

Z = generate(X,Y)


plt.contourf(X,Y,Z, levels=25)
plt.contour(X,Y,Z, levels=25, colors='k', linewidths=0.4)
plt.axis('off')
plt.gca().set_axis_off()
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0,
            hspace = 0, wspace = 0)
plt.margins(0,0)

plt.savefig('land.png')
#plt.show()
