import glob
import os


def read_data(st):
	read1 = open(st+'/accel.csv')
	read2 = open(st+'/light.csv')
	read3 = open(st+'/GPS.csv')
	write = open(st+'/collection.csv',mode='w')
	write.write('time_Biotrace;accel_x;accel_y;accel_z;lightning;speed_GPS;bearing_GPS\n')
	read1.next()
	l = read1.next().split(';')
	z=0
	x=0
	y=0
	for i in range(2,5):
		if(float(l[i]) > 8.5):
			z=i
			if( z == 2):
				y=4
				x=3
			elif( z == 3):
				x = 4
				y = 2
			elif( z == 4):
				x=2
				y=3
	read1.seek(0)
	read1.next()
	read2.next()
	read3.next()
	for row in read1:
		string1 = row.split(';')
		string2 = read2.next().split(';')
		string3 = read3.next().split(';')
		string1[x] = string1[x].strip('\n')
		string1[y] = string1[y].strip('\n')
		string1[z] = string1[z].strip('\n')
		string2[2] = string2[2].strip('\n')
		string3[6] = string3[6].strip('\n')
		string3[7] = string3[7].strip('\n')
		#print(string1[x].strip('\n'))
		st = string1[0]+';'+string1[x]+';'+string1[y]+';'+string1[z]+';'+string2[2]+';'+string3[6]+';'+string3[7]
		st = st.strip('\n')
		#print(st)
		write.write(st+'\n')



lis=glob.glob('/home/gyanesha/Desktop/trial/CNeRG-project/Data/*')
for i in range(len(lis)):
	routes = []
	for j in range(1,5):
		st = (lis[i]+'/route'+str(j));
		read_data(st)
