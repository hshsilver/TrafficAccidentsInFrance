# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from sklearn.metrics import classification_report
url1 = 'caracteristicsClf.csv'
url11 = 'caracteristicsClfTest.csv'
urlP = 'pca.csv'
urlPT = 'pcaT.csv'
urlT = 'targetClfTest.csv'

def classification():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	#YT = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X#[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y
	X_test=XT#[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	knn=KNeighborsClassifier()
	knn.fit(X_train,Y_train)
	Z=knn.predict(X_test)
	#Y_test
	pd_data = pd.DataFrame(Z,columns=['unscathed','killed','hospital','light'])
	print(pd_data)
	#pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
	print(classification_report(XT['killed'], pd_data['killed']))
def Dtree():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=X[['unscathed', 'killed', 'hospital', 'light']]
	X_test=XT[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	clf = tree.DecisionTreeClassifier()
	clf.fit(X_train,Y_train)
	Z=clf.predict(X_test)
	pd_data = pd.DataFrame(Z,columns=['unscathed','killed','hospital','light'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
	joblib.dump(clf,'Dtree.model')
	print(classification_report(XT['killed'], pd_data['killed']))
def ML():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=Y['killed']
	X_test=XT[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	clf = MLPClassifier()
	clf.fit(X_train,Y_train)
	Z=clf.predict(X_test)
	pd_data = pd.DataFrame(Z,columns=['killed'])
	print(pd_data)
	print(classification_report(XT['killed'], pd_data['killed']))
def process():
	num = 7
	df = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	X = np.array(df[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']])
	pca = decomposition.PCA()
	pca.fit(X)
	print(pca.explained_variance_)
	pca.n_components = num
	X_reduced = pca.fit_transform(X)
	pc = pd.DataFrame(X_reduced)
	pc.to_csv(urlP,encoding="LATIN_1",index=False)
	dfT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	Y = np.array(dfT[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']])
	pcaT = decomposition.PCA()
	pcaT.fit(Y)
	print(pcaT.explained_variance_)
	pcaT.n_components = num
	Y_reduced = pcaT.fit_transform(Y)
	pcT = pd.DataFrame(Y_reduced)
	print(pcT.shape)
	pcT.to_csv(urlPT,encoding="LATIN_1",index=False)
print('processing.......')
#process()
print('training.........')
#ML()				#0.8570357035703571/0
Dtree()			#0.7875787578757876/233
#classification()	#0.8362336233623362/84
