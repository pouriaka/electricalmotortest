import numpy as np
import math
import cmath
import matplotlib.pyplot as plt



S = 30e3 ;
V1 = 2400 ;
V2 = 240 ;
a = V1/V2 ;
Zeq = 1.36 + 15.6j

I2 = S/V2;
I1 = I2/a
PF = np.arange(-0.5, 0.5, 0.001)
V1_list = []
I1_list = []
V1_abs = []
PF2 = []


for i in range(len(PF)):

    PF2.append(math.sqrt(1 - PF[i]**2))
    I1_list.append(I1*(PF[i] + np.sign(PF[i])*1j*PF2[i]))
    V1_list.append(a*V2 + I1_list[i]*Zeq)
    V1_abs.append(math.sqrt((V1_list[i].real ** 2) + (V1_list[i].imag ** 2)))

#plot
plt.plot(PF,V1_abs)
plt.show()




