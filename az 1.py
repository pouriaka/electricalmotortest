import numpy as np
import math
import matplotlib.pyplot as plt


V1=4160
nr=1725
f=60
R1=0.521
R2=1.32
X1=4.98
X2=5.32
Xm=136
prot=3.5 * (10**3)
ns = []
ns = np.arange(1725, 2500, 10)
Rth=((Xm/(X1+Xm))**2)*R1
Vth=(Xm/(X1+Xm))*V1


s = []
Ir = []
Pw = []
Pin = []
Pout = []
eta = []

for i in range(len(ns) - 1):
    s.append((ns[i] - nr) / ns[i])
s.remove(0)



for i in range(len(s) - 1):
    Ir.append( Vth / math.sqrt(((Rth + R2 / s[i]) ** 2) + (X1 + X2) ** 2))

    Pin.append ((Ir[i] ** 2) * (R1 + R2 / s[i]))
    Pw.append ((Ir[i] ** 2) * (R1 + R2))

    Pout.append( Pin[i] - Pw[i] - prot)
    eta.append ((Pout[i] / Pin[i]) * 100)



#plot
ns = np.arange(1755, 2500, 10)

plt.plot(ns , Pin)
plt.plot(ns , Pout)
plt.plot(ns , eta)
plt.show()
