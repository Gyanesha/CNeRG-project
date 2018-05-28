import glob
import os
import numpy as np
from scipy.stats import kurtosis

lis=glob.glob('/home/gyanesha/Desktop/trial/CNeRG-project/Data/*')

def deMux(st):
	for i in range(1,5):
		s = st+'/route'+str(i)+'/collection.csv'
		s2 = st+'/route'+str(i)+'/strees_non-stress.csv'
		rs = st+'/route'+str(i)+'/stats.csv'
		process(s,s2,rs)

def process(re,re2,wr):
	read = open(re,mode='r')
	read1 = open(re2,mode='r')
	write = open(wr,mode='w')
	
	
	write.write('median(time1,time1+559);mean(AccX);var(AccX);kurtosis(AccX);EightythPercentile(AccX);mean(AccY);var(AccY);kurtosis(AccY);EightythPercentile(AccY);mean(AccZ);var(AccZ);kurtosis(AccZ);EightythPercentile(AccZ);mean(light);var(light);kurtosis(light);EightythPercentile(light);mean(speed);var(speed);kurtosis(speed);EightythPercentile(speed);mean(bearing);var(bearing);kurtosis(bearing);EightythPercentile(bearing);stressOrNonStress\n')
	read1.readline()
	data=[]
	length=0
	for row in read:
		length+=1
		line=row.split(';')
		data.append(line)

	for i in range(1,length,20):
		stress=read1.readline().split(';')

		if(i+559 >= length):
			break
		hold=[]
		accelx=[]
		accely=[]
		accelz=[]
		light=[]
		speed=[]
		bearing=[]
		for j in range(i,i+560):
			accelx.append(float(data[j][1]))
			accely.append(float(data[j][2]))
			accelz.append(float(data[j][3]))
			light.append(float(data[j][4]))
			speed.append(float(data[j][5]))
			bearing.append(float(data[j][6]))

		t = data[int((2*i+559)/2)][0]
		write.write(t+';'+str(np.mean(accelx))+';'+str(np.var(accelx))+';'+str(kurtosis(accelx))+';'+str(np.percentile(accelx,80))+';'+str(np.mean(accely))+';'+str(np.var(accely))+';'+str(kurtosis(accely))+';'+str(np.percentile(accely,80))+';'+str(np.mean(accelz))+';'+str(np.var(accelz))+';'+str(kurtosis(accelz))+';'+str(np.percentile(accelz,80))+';'+str(np.mean(light))+';'+str(np.var(light))+';'+str(kurtosis(light))+';'+str(np.percentile(light,80))+';'+str(np.mean(speed))+';'+str(np.var(speed))+';'+str(kurtosis(speed))+';'+str(np.percentile(speed,80))+';'+str(np.mean(bearing))+';'+str(np.var(bearing))+';'+str(kurtosis(bearing))+';'+str(np.percentile(bearing,80))+';'+str(stress[1]).strip('\n')+'\n')
		

for i in range(len(lis)):
	st = lis[i]
	deMux(st)