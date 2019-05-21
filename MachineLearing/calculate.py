import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
url1 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristics.csv'
df = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
#print(list(df.an).count(16))
name = ['an','mois','lum','int','atm','col','catr','circ','vosp','prof','plan','lartpc','larrout','surf','infra','situ','env1']
'''
f = open('C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//StatisticalData.txt','a')
for i in range(len(name)):
	print(name[i])
	f.write(str(name[i])+'\n')
	num = 0
	max = 0
	for index in range(df.loc[:,name[i]].min(),df.loc[:,name[i]].max()+1):
		if list(df.loc[:,name[i]]).count(index) != 0:
			f.write(str(index) + '	' + str(list(df.loc[:,name[i]]).count(index)) + '\n')
			if list(df.loc[:,name[i]]).count(index) > max:
				max = list(df.loc[:,name[i]]).count(index)
				num = index
	f.write('Max:	' + str(num) + "	" + str(max) + '\n')
f.close()
'''
df.an.hist()