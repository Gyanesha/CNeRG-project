import glob
import os
import numpy as np
from scipy.stats import kurtosis

lis=glob.glob('/home/gyanesha/Desktop/trial/CNeRG-project/Data/*')

def deMux(st):
	for i in range(1,5):
		s = st+'/route'+str(i)+'/collection.csv'
		rs = st+'/route'+str(i)+'/stats.csv'
		process(s,rs)

def process(re,wr):
	read = open(re,mode='r')
	write = open(wr,mode='w')
	
	
	write.write('((time1+time2)*0.5);mean(AccX);var(AccX);kurtosis(AccX);EightythPercentile(AccX);mean(AccY);var(AccY);kurtosis(AccY);EightythPercentile(AccY);mean(AccZ);var(AccZ);kurtosis(AccZ);EightythPercentile(AccZ);mean(light);var(light);kurtosis(light);EightythPercentile(light);mean(speed);var(speed);kurtosis(speed);EightythPercentile(speed);mean(bearing);var(bearing);kurtosis(bearing);EightythPercentile(bearing)\n')
	
	data=[]
	length=0
	for row in read:
		length+=1
		line=row.split(';')
		data.append(line)

	for i in range(1,length,20):
		if(i+559 >= length):
			break
		hold=[]
		t1=""
		t2=""
		accelx=[]
		accely=[]
		accelz=[]
		light=[]
		speed=[]
		bearing=[]
		for j in range(i,i+560):
			if (j == i):
				t1=data[j][0]
			if (j == i+559):
				t2=data[j][0]
			accelx.append(float(data[j][1]))
			accely.append(float(data[j][2]))
			accelz.append(float(data[j][3]))
			light.append(float(data[j][4]))
			speed.append(float(data[j][5]))
			bearing.append(float(data[j][6]))
		t1=t1.split(':')
		t2=t2.split(':')
		t = str(int(int(t1[0])+int(t2[0]))/2)+':'+str(int(int(t1[1])+int(t2[1]))/2)+':'+str(int(int(t1[2])+int(t2[2]))/2)+':'+str(int(int(t1[3])+int(t2[3]))/2)
		write.write(t+';'+str(np.mean(accelx))+';'+str(np.var(accelx))+';'+str(kurtosis(accelx))+';'+str(np.percentile(accelx,80))+';'+str(np.mean(accely))+';'+str(np.var(accely))+';'+str(kurtosis(accely))+';'+str(np.percentile(accely,80))+';'+str(np.mean(accelz))+';'+str(np.var(accelz))+';'+str(kurtosis(accelz))+';'+str(np.percentile(accelz,80))+';'+str(np.mean(light))+';'+str(np.var(light))+';'+str(kurtosis(light))+';'+str(np.percentile(light,80))+';'+str(np.mean(speed))+';'+str(np.var(speed))+';'+str(kurtosis(speed))+';'+str(np.percentile(speed,80))+';'+str(np.mean(bearing))+';'+str(np.var(bearing))+';'+str(kurtosis(bearing))+';'+str(np.percentile(bearing,80))+'\n')
		

for i in range(len(lis)):
	st = lis[i]
	deMux(st)