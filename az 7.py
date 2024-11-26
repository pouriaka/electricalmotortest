import numpy as np
import math
import matplotlib.pyplot as plt


P = 5000000
Vl = 4160
Ib = P/(Vl*math.sqrt(3))
i1 = 169
i2 = 192
Xu = (i1/i2)

P = []
Ia = []
Ef = []
Ef_andaze = []
If = []
If_real = []


for i in range(0,100):
    P.append((i)/100)
    print(P)
    Ia.append(P[i]/1)
    Ef.append(1 - (1j*Xu*Ia[i]))
    print(Ef)
    Ef_andaze.append(math.sqrt(Ef[i].real**2 + Ef[i].imag**2))
    print(Ef_andaze)
    If.append(Ef_andaze[i]/i1)
    print(If)




plt.plot(P,If)
plt.show()


