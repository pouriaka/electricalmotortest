import numpy as np
import math
import matplotlib.pyplot as plt

Xs  = 1.35
Xeq = 0.23
Xt = Xeq + Xs
Vp = 1.0
Ef = 1.0
I= 297
Vt = 1.0

Ia = []
V = []
Va = []
P = []


delta = np.arange(0 , 3.14/2 , 3.14/100)
print(delta)

for i in range(len(delta)):
    Ia.append((Ef * (2.718 ** (1j * delta[i])) - Vp) / (Xt))
    V.append(Vp + 1j * Xeq * Ia[i])
    Va.append(math.sqrt((V[i].real ** 2) + (V[i].imag ** 2)))
    P.append(Va[i]*Ia[i].real)
    print(P)


P_2 = np.arange(0 , 1 , 0.01)
del_2 = []
Ia_2 = []
Ef_2 = []
If_2 = []
for i in range(len(P_2)):
    del_2.append(math.asin(P_2[i]* Xeq/(Vt*Vp)))
    Ia_2.append((Vt * 2.718 ** (1j * del_2[i] ) - Vp)/(1j * Xeq))
    Ef_2.append(math.sqrt(((Vt + 1j*(Xs+Xeq) * Ia_2[i]).real**2) + ((Vt + 1j*(Xs+Xeq) * Ia_2[i]).imag**2)))
    If_2.append(I * Ef_2[i])

#plot
plt.subplot(1, 2, 1)
plt.plot(P,Va)
plt.subplot(1, 2, 2)
plt.plot(P_2,If_2)
plt.show()
