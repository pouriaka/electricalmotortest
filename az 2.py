import numpy as np
import math
import matplotlib.pyplot as plt



R2 = 1
Poles = 4
P2 = 12000
fs = 50
V1 = 250
Vs = V1 / math.sqrt(3)
R1 = 0.1
X1 = 0.7
X2 = 0.67
Xm = 18.7
DPmech = 250
DPcore = 200
Ns = 120 * fs / Poles
Vth = (Vs * Xm) / math.sqrt(R1**2 + (Xm + X1)**2)
Rth = (Xm / (X1 + Xm)) ** 2 * R1
Xth = X1
Nr = np.arange(0, 1500, 1)
s = []
Tmech = []
Pmech = []

for i in Nr:
    s.append((Ns - Nr[i]) / Ns)
    Tmech.append((3 * R2 * (Vth ** 2) / 2 * 3.14 * Ns * s[i] ) / (((Rth + R2 / s[i]) ** 2) + ((Xth + X2) ** 2)) )
    Pmech.append((( 3 * (Vth ** 2) * ( 1 - s[i])) / s[i]) / ((((Rth * R2) / s[i]) ** 2) + (Xth + X2) ** 2) - 250)

print(s)
print(Pmech)
print(Tmech)

#plot
plt.plot(Nr , Pmech)
plt.show()

