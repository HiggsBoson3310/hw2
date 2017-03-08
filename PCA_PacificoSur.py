#Importamos los paquetes necesarios para resolver el problema
import matplotlib.pyplot as plt
import numpy as np
#Leemos los datos guardandolos en listas
heat, SOI = open('heat_content_index.txt').readlines(), open('SOI.txt').readlines()
mh = []
Ta1 = []
Ta2 = []
Ta3 = [] #lista que contendra el promedio de las anomalias de temperatura para cada anho, el promedio se realiza teniendo en cunate cada mes
ms = [] #anhos contemplados en el estudio SOI
Ss = []#valores promedio de SOI, promedio de los doce meses del anho.
#Primero organicemos los datos de las anomalias de temperatura. 

for i in range(len(heat)):
	try:
		data = []
		line = heat[i].split()
		for j in range(len(line)):
			data.append(float(line[j]))
		if(len(mh)==0): mh.append(0)
		else: mh.append(mh[len(mh)-1]+1)
		Ta1.append(data[2])
		Ta2.append(data[3])
		Ta3.append(data[4])
	except ValueError:
		continue


for i in range(len(SOI)):
	try:
		data = []
		line = SOI[i].split()
		for k in range(len(line)):
			data.append(float(line[k]))
		if(data[0]>=1979):
			for j in range(1,len(data)):
				Ss.append(data[j])
				if(len(ms)==0): 
					ms.append(0)
				else: 
					ms.append(ms[len(ms)-1]+1)
	except ValueError:
		continue

	
plt.figure(figsize=(30,8))
plt.grid(True)
plt.title('Anomalias Termicas Mensuales desde Enero de 1979-Febrero 2017')
plt.xlabel('Tiempo (meses)')
plt.ylabel('Anomalia (C)') 
plt.plot(mh,Ta1,label="Anomalia en 130E-80W")
plt.plot(mh,Ta2,label="Anomalia en 160E-80W")
plt.plot(mh,Ta3,label="Anomalia en 180E-100W")
plt.plot(ms,Ss,label='SOI')
plt.legend(loc=0)
plt.savefig("Anomalies_SOI_Plot.pdf")
plt.close()
print type(Ta1[9])
Md = np.array([np.array(Ta1),np.array(Ta2),np.array(Ta3),np.array(Ss)])
Cov_matrix = np.cov(Md)
Eval, Evec = np.linalg.eig(Cov_matrix)
NewData = np.dot(Evec,Md)
plt.scatter(NewData[0,:],NewData[1,:],s=0.5)
plt.show()































