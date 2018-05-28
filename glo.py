import glob
import os
lis=glob.glob('/home/gyanesha/Desktop/trial/CNeRG-project/Data/*')
#print(lis)


def read_process( inp,out,out2):
	data = []
	length = 0
	k=0
	for row in inp:
		length+=1
		line=row.split(';')
		data.append([line[0],line[4],line[5]])
	for i in range(1,length,20):
		if(i+559 > length):
			break
		k+=1
		p1=0
		p2=0
		p3=0
		p4=0
		rmssd1=0
		rmssd2=0
		rmssd3=0
		rmssd4=0
		t1=""
		t2=""
		t1=data[i][0]
		j=0
		for j in range(i,i+560):
			if (j < length):
				if (j >= i) and (j<(i+140)):
					p1+=float(data[j][1])
					if (j is not i):
						rmssd1+=(60000/float(data[j][1])-60000/float(data[j-1][1]))*(60000/float(data[j][1])-60000/float(data[j-1][1]))
				elif (j >= i+140) and (j<(i+280)):
					p2+=float(data[j][1])
					if (j is not i+140):
						rmssd2+=(60000/float(data[j][1])-60000/float(data[j-1][1]))*(60000/float(data[j][1])-60000/float(data[j-1][1]))
				elif((j >= i+280) and (j<(i+420))):
					p3+=float(data[j][1])
					if (j is not i+280):
						rmssd3+=(60000/float(data[j][1])-60000/float(data[j-1][1]))*(60000/float(data[j][1])-60000/float(data[j-1][1]))
				elif((j >= i+420) and (j<(i+560))):
					p4+=float(data[j][1])
					if (j is not i+420):
						rmssd4+=(60000/float(data[j][1])-60000/float(data[j-1][1]))*(60000/float(data[j][1])-60000/float(data[j-1][1]))
				
				#if (j is not i):
				#	rmssd+=(60000/float(data[j][1])-60000/float(data[j-1][1]))*(60000/float(data[j][1])-60000/float(data[j-1][1]))
				
				
			else:
				j-=1
				break
		#if (i+559)<length:
		rmssd1/=139
		rmssd4/=139
		rmssd3/=139
		rmssd2/=139
		rmssd1=rmssd1**(0.5)
		rmssd2=rmssd2**(0.5)
		rmssd3=rmssd3**(0.5)
		rmssd4=rmssd4**(0.5)
		t2=data[j][0]
		time2=t2.split(':')
		for j in range(len(time2)):
			time2[j] = int(time2[j])
		time1=t1.split(':')
		for j in range(len(time1)):
			time1[j] = int(time1[j])
		difference=data[int((2*i+559)/2)][0]
		
		p1/=140
		p2/=140
		p3/=140
		p4/=140
		stress=0
		if (p4 > 1.05*p1) and (rmssd3 > 1.09*rmssd4):
			stress =1
		out2.write(difference+';'+str(stress)+'\n')
		out.write(str(k)+";"+t1+";"+t2+";"+(difference)+";"+str(p1)+";"+str(p2)+";"+str(p3)+";"+str(p4)+";"+str(rmssd1)+";"+str(rmssd2)+";"+str(rmssd3)+";"+str(rmssd4)+";"+str(stress)+"\n")
	#print(data)

for z in range(len(lis)):
	
	s=lis[z]
	routes = []
	for i in range(0,4):
		routes.append(s+'/route'+str(i+1))

	for i in range(0,4):
		st=routes[i]+"/biologicalData.csv"
		re=open(st,mode='r')
		stw=routes[i]+"/process.csv"
		wr=open(stw,mode='w')
		if os.path.exists(routes[i]+"/strees_non-stress.csv"):
			os.remove(routes[i]+"/strees_non-stress.csv")
		st2 = routes[i]+"/stress_non-stress.csv"
		wr2 = open(st2,mode='w')
		wr2.write("median(time1,time2);stress/non-stress\n")
		wr.write("Serial_no.;time1;time2;median(time1,time2);mean(HR1);mean(HR2);mean(HR3);mean(HR4);RMSSD1;RMSSD2;RMSSD3;RMSSD4;stress/non-stress\n")
		read_process(re,wr,wr2)
		