import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2.,80)
nx = 80
dx = 2./(nx-1)
nt = 20
dt = .001
c = 1
u =  np.ones(nx)
u[int(0.5/dx):int(1/dx+1)] = 2.0
plt.plot(x,u)
plt.show()
plt.title("Linear")
for i in range(nt):
	un = u.copy()
	for k in range(1,nx):
		u[k] = un[k]-c*(dt/dx)*(un[k]-un[k-1])
	ut = u.copy()	
plt.plot(x,ut)
plt.show() 
Unl =  np.ones(nx)
Unl[int(0.5/dx):int(1/dx+1)] = 2.0
plt.close()
plt.title("Non linear")
for n in range(nt):
	un = Unl.copy()
	for i in range(1,nx):
		Unl[i] = un[i]-un[i]*(dt/dx)*(un[i]-un[i-1])
	ut = Unl.copy()	
plt.plot(x,ut)
plt.show() 
nu = 0.3
d = np.ones(nx)
d[int(0.5/dx):int(1/dx+1)] = 2.0
for n in range(nt):
	dn = d.copy()
	for i in range(1,nx-1):
		d[i] = dn[i]+nu*(dt/dx**2)*(dn[i+1]-2*dn[i]+d[i-1])
plt.close()
plt.title("Diffusion")
plt.plot(x,d)
plt.show()

