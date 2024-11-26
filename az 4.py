import numpy as np
import math
import matplotlib.pyplot as plt


V_L_OC1 = [2.27 , 4.44 , 6.68 , 8.67 , 10.4 , 11.9 , 13.4 , 14.3 , 14.5]
V_L_OC2 = []
If = [100 , 200 , 300 , 400 , 500 , 600 , 700, 775 , 800]
If1 = [0 , 710]
Ia = [0 , 6070]
for i in range(len(If) ):
    V_L_OC2.append(0.0217 * If[i] + 0.1)


#plot
plt.plot(If,V_L_OC1)
plt.plot(If,V_L_OC2)
plt.show()

