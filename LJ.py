import numpy as np 
import matplotlib.pyplot as plt 
#Lennard Jones Plot
r= np.linspace(0.01, 3.0, num=500)
epsilon=1
sigma=1

Elj= 4*epsilon*((sigma/r)**12 - (sigma/r)**6)

plt.plot(r, Elj, color='red', label=' epsilon=1 sigma=1 ')

#For different values of sigma and epsilon------------------
epsilon=0.9
sigma=2
Elj= 4*epsilon*((sigma/r)**12 - (sigma/r)**6)
plt.plot(r, Elj, color='blue', label='Epsilon=0.9 Sigma=2')

epsilon=1.489999
sigma=0.25
Elj= 4*epsilon*((sigma/r)**12 - (sigma/r)**6)
plt.plot(r, Elj, color='green', label='Epsilon=1.489999 Sigma=0.25')
#-----------------------------------------------------------
Rcutoff = 2.5
phicutoff=4.0/(Rcutoff**12)-4.0/(Rcutoff**6)

Elj_shift = Elj -phicutoff 

plt.plot(r[:415], Elj_shift[:415], 'b-', linewidth=1) 

plt.title("Lennard-Jones Potential") 
plt.xlim(0.0, 3.0)
plt.ylim(-1.5, 1.5)

plt.ylabel('Epsilon', color='red', fontsize=20)
plt.xlabel('Sigma', color='red', fontsize=20)

plt.legend(frameon=False, fontsize=20)

plt.axhline(0, color='grey', linestyle='--', linewidth=2)

plt.axvline(1, color='grey', linestyle='--', linewidth=2)

plt.legend(loc='best')

plt.show()

