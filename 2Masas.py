#Importamos los paquetes necesarios para resolver el problema 
import numpy as np
import matplotlib.pyplot as plt
#Definimos la funcion solve, que toma como paramentros los pesos (en N), separacion y longitudes de cuerda (en m), y un vector guess de la solucion (en el orden especifio de la solucion), y retorna un vector que contiene  los valores de las incongnitas en el siguiente orden: T1,T2,T3,sin(\theta_1),sin(\theta_2), sin(\theta_3), cos(\theta_1),cos(\theta_2) y cos(\theta_3) utilizando el metodo de Newton multidimensional. 

def solve(w,W,l,l1,l2,l3,guess):
	sol = []
	vguess = []
	it = []
	th1 = []
	th2 = []
	th3 = []
	T1 = []
	T2 = []
	T3 = []
	for i in range(len(guess)):
		vguess.append([guess[i]])
	vguess = np.array(vguess)
		

	def f(z):
		f1 = l1*z[6]+l2*z[7]+l3*z[8]-l
		f2 = l1*z[3]+l2*z[4]-l3*z[5]
		f3 = (z[3]**2)+(z[6]**2)-1
		f4 = (z[4]**2)+(z[7]**2)-1
		f5 = (z[5]**2)+(z[8]**2)-1
		f6 = z[0]*z[3]-z[1]*z[4]-w
		f7 = z[0]*z[6]-z[1]*z[7]
		f8 = z[1]*z[4]+z[2]*z[5]-W
		f9 = z[1]*z[7]-z[2]*z[8]
		return np.array([f1,f2,f3,f4,f5,f6,f7,f8,f9])
	def partial(f,i,z,h):
		dz = np.zeros(9)
		dz[i] = h
		d = (f(z+dz)-f(z))/h
		return d
	b=[[1]]
	s = 0
	while(np.linalg.norm(b)>1e-3 and s<1e3):
		th1.append(np.arccos(vguess[6,0])*180./np.pi)
		th2.append(np.arcsin(vguess[4,0])*180./np.pi)
		th3.append(np.arccos(vguess[8,0])*180./np.pi)
		T1.append(vguess[0])
		T2.append(vguess[1])
		T3.append(vguess[2])		
		it.append(s)
		D = []
		b = [] 
		for i in range(9):
			D.append(partial(f,i,vguess[:,0],0.01))
		D = np.array(D).T
		for i in range(len(f(vguess[:,0]))):
			b.append([-f(vguess[:,0])[i]])
		b=np.array(b)
		sol = np.linalg.solve(D,b)
		vguess = vguess+sol
		
		s += 1
	plt.grid(True)
	plt.title("Angulos de Cuerdas por Iteracion")
	plt.xlabel("Iteraciones")
	plt.ylabel("Angulo (grados)")
	plt.plot(it,th1,label='$\\theta_1$',color='b')
	plt.plot(it,th2,label='$\\theta_2$',color='r')
	plt.plot(it,th3,label='$\\theta_3$',color='g')
	plt.legend(loc=0)
	plt.savefig('AnglesPLOTS.pdf')
	plt.close()
	plt.grid(True)
	plt.title("Tension en Cuerdas por Iteracion")
	plt.xlabel("Iteraciones")
	plt.ylabel("Tension (N)")
	plt.plot(it,T1,label='$T_1$',color='b')
	plt.plot(it,T2,label='$T_2$',color='r')
	plt.plot(it,T3,label='$T_3$',color='g')
	plt.legend(loc=0)
	plt.savefig('TensionPLOTS.pdf')
	plt.close()
	return vguess
	


solve(10.,20.,8.,3.,4.,4.,np.array([100,100,100,0.5,0.5,0.5,np.sqrt(0.75),np.sqrt(0.75),np.sqrt(0.75)]))
