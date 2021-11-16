
""" Code for SIR model for Covid -19 in a closed society in nigeria """

import math
import matplotlib.pyplot as plt
"""susceptible (S) individuals by x, the number of infected (I) individuals
                   by y, and the number of recovered or removed (R) individuals by z"""
N = 3127                 #number of population
x = N-10
y = 10
z = 0
taxis=[ ]
xaxis=[ ]
yaxis=[ ]
zaxis=[ ]
beta=.3/N             #contact rate
gamma=0.1              #removed rate (dead or recovered)
dt=0.001               #Time step
t = 0
cnt=0                  #Count

""" Loop for solving the equations using Runge -Kutta method"""

while t<60:
 if cnt%100==0:
  taxis.append(t)
  xaxis.append(x)
  yaxis.append(y)
  zaxis.append(z)
  # step 1
 kx1 = - beta*x*y                 #susceptible ds(t)/dt
 ky1 = beta*x*y - gamma*y         #infected dI (t)/dt
 # step 2
 t2 = t+dt
 x2 = x + kx1*dt
 y2 = y + ky1*dt
 kx2 = - beta*x2*y2
 ky2 = beta*x2*y2 - gamma*y2
 # update
 x = x + (kx1+kx2)*dt/2                      #number of susceptible
 y = y + (ky1+ky2)*dt/2                      #Number of infected
 z = N - x - y                               #Number of recovered
 t = t + dt
 cnt = cnt + 1

 """ Plotting the equations to obtain SIR plot """

plt.title("SIR MODEL(Runge-Kutta) using beta=.3 gamma=.1")
plt.plot(taxis,xaxis, color=(0,1,0), linewidth=1.0, label="S")
plt.plot(taxis,yaxis, color=(1,0,0), linewidth=1.0, label="I")
plt.plot(taxis,zaxis, color='green', linestyle='dashed', linewidth = 1, label="R")
plt.xlim(0,60)
plt.legend()
plt.xlabel("DAY")
plt.ylabel("susceptible S(t),infected I(t),recovered R(t)")
plt.grid(True)
plt.show()