import numpy as np
import math
import cmath
import matplotlib.pyplot as plt

V = 8
Rl = 50

N2 = 1
N1 = np.arange(1, 13, 1)

a_1 =[]
Rl2_1 = []
Z_1 = []
I_1 = []
P_1 = []


for i in range(len(N1)):
    a_1.append(N1[i]/N2)
    Rl2_1.append(a_1[i]**2 * Rl)
    Z_1.append(2000 + Rl2_1[i])
    I_1.append(V/Z_1[i])
    P_1.append(Rl2_1[i]*I_1[i]**2)





a_2 =[]
Rl2_2 = []
Z_2 = []
I_2 = []
P_2 = []
I_abs = []


for i in range(len(N1)):
    a_2.append(N1[i]/N2)
    Rl2_2.append(a_2[i]**2 * Rl)
    Z_2.append(2000j + Rl2_2[i])
    I_2.append(V/Z_2[i])
    I_abs.append(math.sqrt((I_2[i].real ** 2) + (I_2[i].imag ** 2)))
    P_2.append(Rl2_2[i]*I_abs[i]**2)



plt.plot(a_1,P_1)
plt.plot(a_2,P_2)
plt.show()