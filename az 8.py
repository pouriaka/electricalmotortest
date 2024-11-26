import numpy as np
import math
import cmath
import matplotlib.pyplot as plt



Vb = 2300;
Sb = 750e3;
Zb = Vb**2/Sb;
Xs = 7.75/Zb;
P = 600e3/Sb;
Vt = 1
AF = 120


theta = np.arange(1 , -1 , -0.01)
PF_theta = []
Eaf = []
Eaf_andaze = []
Ia = []
Ia_dekarti = []
Eaf_abs = []
If = []
theta_2 = []

for i in range(len(theta)):
    theta_2.append(theta[i] - 0.0000000e-01)
    PF_theta.append(math.acos(0.8)*theta_2[i])
    Ia.append(P/(Vt * math.cos(theta_2[i])))
    Ia_dekarti.append(cmath.rect(Ia[i],math.acos(theta_2[i])))
    Eaf.append(Vt + Xs*Ia_dekarti[i])
    Eaf_abs.append(math.sqrt((Eaf[i].real**2) + (Eaf[i].imag**2)))
    If.append(Eaf_abs[i] * AF)

#plot
plt.plot(If,Ia)
plt.show()




