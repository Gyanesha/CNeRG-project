import glob
import os
from math import sin, cos, sqrt, atan2, radians


lis=glob.glob('/home/gyanesha/Desktop/trial/CNeRG-project/Data/*')
#print(lis)

def findDist(lati1,long1,lati2,long2):
	lati1=radians(lati1)
	long1=radians(long1)
	lati2=radians(lati2)
	long2=radians(long2)
	dlon =long2-long1
	dlat =lati2-lati1
	R = 6373.0
	#dist = 6371.01 * acos(sin(lati1)*sin(lati2) + cos(lati1)*cos(lati2)*cos(long1 - long2))
	a = sin(dlat / 2)**2 + cos(lati2) * cos(lati1) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = R * c
	return distance

def timeDiff(time1,time2):
	t1=[]
	t2=[]
	for i in time1.split(':'):
		t1.append(int(i))

	for i in time2.split(':'):
		t2.append(int(i))
	
	if (t2[3] < t1[3]):
		t2[2]-=1
		t2[3]+=1000
	t2[3]-=t1[3]

	if(t2[2] < t1[2]):
		t2[1]-=1
		t2[2]+=60
	t2[2]-=t1[2]

	if(t2[1] < t1[1]):
		t2[0]-=1
		t2[1]+=60
	t2[1]-=t1[1]

	t2[0]-=t1[0]
	return (str(t2[0])+':'+str(t2[1])+':'+str(t2[2])+':'+str(t2[3]))

	 

def readAndWrite(wr,list3):
	write = open(wr,mode='w')
	t=""
	write.write("TripNo.;Intertrip_Time;Trip_Time;Trip_Distance\n")
	qw = open("/home/gyanesha/Desktop/raw.csv",mode='w')
	for i in range(len(list3)):
		st = list3[i]+'/GPS.csv'
		read = open(st,mode='r')
		data = []
		inter_time="00:00:00:0000"	
		read.next()
		l = read.next().split(';')
		
		lat1=float(l[2])
		long1=float(l[3])
		distance=0
		time= l[0]
		if(i != 0):
			inter_time=timeDiff(t,time)
		for j in read:
			line = j.split(';')
			t = line[0]
			lat2 = float(line[2])
			long2 = float(line[3])
			distance+= findDist(lat1,long1,lat2,long2)

			qw.write(str(findDist(lat1,long1,lat2,long2))+"	"+str(distance)+'\n')
			lat1=lat2
			long1=long2
			#print(findDist(lat1,long1,lat2,long2))
		print(distance)
		time=timeDiff(time,t)
		#print(data[0])
		trip_no=i+1
		write.write(str(trip_no)+";"+inter_time+";"+time+";"+str(distance)+"\n")


for i in range(len(lis)):
	st = lis[i]
	#list2 = glob.glob(st+'/*')
	wr = lis[i]+'/trip_analysis.csv'
	#print(list2)
	list3=[]
	for j in range(4):
		list3.append(lis[i]+"/route"+str(j+1))
	#print(list3)
	readAndWrite(wr,list3)
		#print( re +" "+wr+"\n")

dist=findDist((48.74706937),(9.108210037),(48.74020461),(9.107615656))
print(dist)