import numpy as np
import math
import matplotlib.pyplot as plt


t = np.arange(-0.1 , 0.1 , 0.001)
f = 50;
w = 2* 3.14 *f
V = []
V1 = []
Vt1 = []
Vt2 = []
Vt3 = []
Vt4 = []

#1
for i in range(len(t)):
    V.append(220* math.cos(w*t[i]));
    V1.append(220 * math.cos(w * t[i] + (4 * 3.14 / 3)))
    Vt1.append(V[i] + V1[i])

#plot
plt.plot(t,V)
plt.plot(t,Vt1)
plt.show()


#2
f1 = 0.5*f
w2 = 2*3.14*f1
V2 = []
for i in range(len(t)):
    V2.append(220*math.cos(w2*t[i]))
    Vt2.append(V[i] + V2[i])

#plot
plt.plot(t,V)
plt.plot(t,Vt2)
plt.show()

#3
V3 = []
for i in range(len(t)):
    V3.append(V[i] * 1.8)
    Vt3.append(V[i] + V3[i])

#plot
plt.plot(t,V)
plt.plot(t,Vt3)
plt.show()

#4
f2 = 2*f
w4 = 2*3.14*f2
V4 = []
for i in range(len(t)):
    V4.append(2*220*math.cos(w4*t[i]))
    Vt4.append(V[i] + V4[i])

#plot
plt.plot(t,V)
plt.plot(t,Vt4)
plt.show()


