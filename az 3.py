import numpy as np
import math
import matplotlib.pyplot as plt




Vi = 2400
Vs = Vi/math.sqrt(3)
Z = 0.18 + 0.41j
I = Vi/Z
I_conj = np.conj(I)
S = 3 * Vi * I_conj
P2 = np.real(S)
P2 = 15513216.957605988
print(P2)

print(S)
s = np.arange(0.005 , 0.035 , 0.003)
print(s)

Pag = []
P1 = []
eta = []
P = []

for i in range(len(s) - 1):
    Pag.append(P2 / (1 - s[i]))
    P1.append(Pag[i])
    eta.append(P2 / P1[i])
print(P1)
#for i in P1:
   # P.append( P1[i] / 1000000)

#plot
plt.plot(P1,eta)
plt.show()

