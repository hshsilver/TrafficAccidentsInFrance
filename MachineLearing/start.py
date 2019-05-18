# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
url = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//target.csv'
urlReal = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//targetReal.csv'
urlT = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//targetTest.csv'
url1 = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//caracteristics.csv'
url3 = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//users.csv'
url11 = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//caracteristicsTest.csv'
url33 = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//usersTest.csv'
urlP = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//pca.csv'
urlPT = 'C://Users//liuyang//Desktop//France//accidents-in-france-from-2005-to-2016//预处理//pcaT.csv'
def classification():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	#YT = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y
	X_test=XT#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	#Y_test=indices[-10:].reshape(-1,1)
	#Create and fit a nearest-neighbor classifier
	knn=KNeighborsClassifier()
	knn.fit(X_train,Y_train)
	Z=knn.predict(X_test)
	#Y_test
	pd_data = pd.DataFrame(Z,columns=['unscathed','killed','hospital','light'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
def Dtree():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	#YT = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y
	X_test=XT#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	#Y_test=indices[-10:].reshape(-1,1)
	clf = tree.DecisionTreeClassifier()
	clf.fit(X_train,Y_train)
	Z=clf.predict(X_test)
	#Y_test
	pd_data = pd.DataFrame(Z,columns=['unscathed','killed','hospital','light'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
def ML():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	#YT = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y['killed']
	X_test=XT#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	#Y_test=indices[-10:].reshape(-1,1)
	clf = MLPClassifier()
	clf.fit(X_train,Y_train)
	Z=clf.predict(X_test)
	#Y_test
	pd_data = pd.DataFrame(Z,columns=['killed'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
def RandomForest():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y
	X_test=XT#[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	clf = RandomForestClassifier(n_estimators=10)
	clf.fit(X_train,Y_train)
	Z=clf.predict(X_test)
	#Y_test
	pd_data = pd.DataFrame(Z,columns=['unscathed','killed','hospital','light'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
def process():
	num = 7
	df = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	X = np.array(df[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']])
	pca = decomposition.PCA()
	pca.fit(X)
	print(pca.explained_variance_)
	pca.n_components = num
	X_reduced = pca.fit_transform(X)
	pc = pd.DataFrame(X_reduced)
	pc.to_csv(urlP,encoding="LATIN_1",index=False)
	dfT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = np.array(dfT[['lum', 'agg', 'int', 'atm','col', 'com', 'lat', 'long', 'dep', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']])
	pcaT = decomposition.PCA()
	pcaT.fit(Y)
	print(pcaT.explained_variance_)
	pcaT.n_components = num
	Y_reduced = pcaT.fit_transform(Y)
	pcT = pd.DataFrame(Y_reduced)
	print(pcT.shape)
	pcT.to_csv(urlPT,encoding="LATIN_1",index=False)
def test():
	dfT = pd.read_csv(url#T,encoding="LATIN_1",low_memory=False)#iso8859_15
	dfR = pd.read_csv(urlReal,encoding="LATIN_1",low_memory=False)#iso8859_15
	real=[0]*32
	test=[0]*32
	T=[0]*32
	for index in range(len(dfT)):
		name='killed'
		real[dfR.at[index,name]] = real[dfR.at[index,name]] + 1
		T[int(dfT.at[index,name])] = T[int(dfT.at[index,name])] + 1
		if (int(dfT.at[index,name])==dfR.at[index,name]):
			test[dfR.at[index,name]] = test[dfR.at[index,name]] + 1
	print('Death toll     ',' 0	1	2      3    4    5    6   7  8  9  10....')
	print('True death data',real)
	print('Predict data   ',T)
	print('Hit data       ',test)
	rate=0
	for index in range(32):
		rate = rate + test[index]
	print('hit num',rate)
	rate = rate/19998
	print('rate ',rate)
print('processing.......')
#process()
print('training.........')
#ML()				#0.8570357035703571/0	#0.8570357035703571/0		Neural Networks
#Dtree()			#0.7875787578757876/233	#0.741024102410241/519		Decision tree
#classification()	#0.8362336233623362/84	#0.8379837983798379/67		KNN
#RandomForest()		#0.8563856385638564/3	#0.8517851785178517/38		Random Forest
print('test.............')
test()