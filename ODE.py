import numpy as np
import matplotlib.pyplot as plt

def solve(b,y0,f,fr):
	def fillrk(x,y,h):
		xf = x+h/2.
		yf = y+(h/2.)*f(x,y)
		return y+h*f(xf,yf)
	def fillrk4(x,y,h):
		k1 = f(x,y)
		k2 = f(x,y+(h/2.)*k1)
		k3 = f(x,y+(h/2.)*k2)
		k4 = f(x,y+h*k3)
		return y+(1./6.)*(k1+2*(k2+k3)+k4)*h
	t = np.linspace(0,b,1000)
	h = t[1]-t[0]
	if(fr!=0): yr = fr(t)
	ye = [y0]
	ylf = [y0]
	yrk = [y0]
	yrk4 = [y0]
	for i in range(len(t)-1):
		ye.append(ye[i]+h*f(t[i],ye[i]))	
		if(i==0): ylf.append(ye[i+1])
		else: ylf.append(ylf[i-1]+2*h*f(t[i],ylf[i]))
		yrk.append(fillrk(t[i],yrk[i],h))
		yrk4.append(fillrk4(t[i],yrk4[i],h))




	
	if (fr!=0): plt.plot(t,yr,label='real')
	plt.plot(t,ye,label='Euler')
	plt.plot(t,ylf,label='Leap Frog')
	plt.plot(t,yrk,label='Runge-Kutta')
	plt.plot(t,yrk4,label='Runge-Kutta 4')
	plt.legend(loc=0)
	plt.show()
	plt.close()
	if (fr!=0):
		plt.plot(t,abs(np.array(yr)-np.array(ye)),label="Error euler")	
		plt.plot(t,abs(np.array(yr)-np.array(ylf)),label="Error leap frog")
		plt.plot(t,abs(np.array(yr)-np.array(yrk))*1e2,label="Error Runge-Kutta ($\\times 10{-2}$)")
		plt.plot(t,abs(np.array(yr)-np.array(yrk4))*1e11,label="Error Runge-Kutta 4 ($\\times 10{-11}$)")
		plt.legend(loc=0)
		plt.show()
	plt.close

def f(x,y):
	return 1+y**2
def z(x,y):
	return -y
solve(1,0,f,np.tan)
solve(1,1,z,np.exp)

