# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import sklearn

url = 'src/MachineLeaning/ML/visualization.csv'
url1 = 'src/MachineLeaning/ML/graph1.csv'
url2 = 'src/MachineLeaning/ML/graph2.csv'
predictChance = 'src/MachineLeaning/ML/predictChance.csv'

class Accident:
	def __init__(self,Num_Acc,an,mois,jour,hrmn,lum,int,atm,col,lat,long,catr,circ,nbv,vosp,prof,plan,lartpc,larrout,surf,infra,situ,env1):
		self.chance = 1
		self.Num_Acc = Num_Acc
		self.year = an
		self.month = mois
		self.day = jour
		self.time = hrmn
		self.lum = lum
		self.int = int
		self.atm = atm
		self.col = col
		self.lat = lat
		self.long = long
		self.catr = catr
		self.circ = circ
		self.nbv = nbv
		self.vosp = vosp
		self.prof = prof
		self.plan = plan
		self.lartpc = lartpc
		self.larrout = larrout
		self.surf = surf
		self.infra = infra
		self.situ = situ
		self.env1 = env1
	def tolist(self):
		return [self.Num_Acc,self.year,self.month,self.day,self.time,self.lum,self.int,self.atm,self.col,self.lat,self.long,self.catr,self.circ,self.nbv,self.vosp,self.prof,self.plan,self.lartpc,self.larrout,self.surf,self.infra,self.situ,self.env1,self.chance]

def showChart(num):# 1:yyyy-mm-dd 死伤人数 unscathed-killed-hospital-light
	if num == 1:#日期-死伤人数-unscathed-killed-hospital-light
		graph = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
		list = []
		for index in range(len(graph)):
			list.append([])
			list[index].append('20' + str(graph.loc[index,'an']).zfill(2) + '-' + str(graph.loc[index,'mois']).zfill(2) + '-' + str(graph.loc[index,'jour']).zfill(2))
			list[index].append(graph.loc[index,'sum'])
			list[index].append(graph.loc[index,'unscathed'])
			list[index].append(graph.loc[index,'killed'])
			list[index].append(graph.loc[index,'hospital'])
			list[index].append(graph.loc[index,'light'])
		#print(list)
		return list
	elif num == 2:#周几-时间-四类人数
		graph = pd.read_csv(url2,encoding="LATIN_1",low_memory=False)#iso8859_15
		unscathed = []
		killed = []
		hospital = []
		light = []
		for index in range(len(graph)):
			unscathed.append([])
			killed.append([])
			hospital.append([])
			light.append([])
			unscathed[index].append(graph.loc[index,'week'])
			unscathed[index].append(graph.loc[index,'time'])
			unscathed[index].append(graph.loc[index,'unscathed'])
			killed[index].append(graph.loc[index,'week'])
			killed[index].append(graph.loc[index,'time'])
			killed[index].append(graph.loc[index,'killed'])
			hospital[index].append(graph.loc[index,'week'])
			hospital[index].append(graph.loc[index,'time'])
			hospital[index].append(graph.loc[index,'hospital'])
			light[index].append(graph.loc[index,'week'])
			light[index].append(graph.loc[index,'time'])
			light[index].append(graph.loc[index,'light'])
		return unscathed, killed, hospital, light
	elif num == 3:#yyyy-mm-dd 相关人数
		graph = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
		list = []
		for index in range(len(graph)):
			list.append([])
			list[index].append('20' + str(graph.loc[index,'an']).zfill(2) + '-' + str(graph.loc[index,'mois']).zfill(2) + '-' + str(graph.loc[index,'jour']).zfill(2))
			list[index].append(graph.loc[index,'unscathed'] + graph.loc[index,'killed'] + graph.loc[index,'hospital'] + graph.loc[index,'light'])
		print(list)
		return list

def showAll():
	detail = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	detail = detail[['Num_Acc','lat','long']]
	return detail.values.tolist()
def showDetail(Num_Acc):
	detail = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	detail = detail[detail['Num_Acc'].isin([Num_Acc])]
	return detail.values.tolist()
	
def predictTheProbability():#accident对象的数组
	df = pd.read_csv(predictChance,encoding="LATIN_1",low_memory=False)#iso8859_15
	MLP = joblib.load('src/MachineLeaning/ML/Regression.model')
	X_test = df[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Z = MLP.predict(X_test)#list
	for i in range(len(Z)):
		if Z[i] < 0:
			Z[i] = 0
		elif Z[i] > 1:
			Z[i] = 1
	X_position = df[['lat', 'long','chance']]
	X_position['chance'] = pd.DataFrame(Z,columns=['chance'])
	return X_position.values.tolist()

def predictDeaths(accident):#accident对象的数组
	MLD = joblib.load('src/MachineLeaning/ML/Dtree.model')
	df = pd.DataFrame(columns=('Num_Acc','an','mois','jour','hrmn','lum', 'int', 'atm','col', 'lat', 'long', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1', 'chance'))
	for index in range(len(accident)):
		df.loc[index] = accident[index].tolist()
	X_test = df[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	#print(X_test)
	P = MLD.predict(X_test)#list
	return P
def upload(accident,injury):#accident对象
	df = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	num = df.shape[0] + 1
	data = accident.tolist()
	for i in range(len(injury)):
		data.append(injury[i])
	df.loc[num] = data
	df.to_csv(url,encoding="LATIN_1",index=False)


#a = Accident(202000000022,16,4,2,1045,1,2,1,3,5084579,226407,3,2,2,0,2,1,0,73,1,0,0,0)
#b = [a]
#print(predictTheProbability(b))
#print(predictDeaths(b))
#print(showChart(3))
#print(showDetail(201600000022))
#upload(a,[5,2,1,3])