import numpy as np
import matplotlib.pyplot as plt
x= np.array([10,20,30,40,50])
y = np.array([1,2,3,4,5])
plt.scatter(x,y,marker='x' , c='b')
plt.title('page counter ')
plt.xlabel('thickness')
plt.ylabel('page')
plt.show()
w = 0.1
b = 0
def c(x,w,b):
    m =  x.shape[0]
    f = np.zeros(m)
    for i in range(m):
        f[i] =  w * x[i]  + b
    return f
k = c(x,w,b)
plt.plot(x,k,label='count' , c='g')
plt.scatter(x,y,marker='x' , c='b')
plt.title('page counter ')
plt.xlabel('thickness')
plt.ylabel('page')
plt.show()
z = int(input("values"))
t = w * z + b
print(t)