# coding: utf-8
import numpy as np
import pandas as pd
from sklearn import decomposition
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import svm
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
url = 'target.csv'
urlReal = 'targetReal.csv'
urlT = 'targetRegTest.csv'
url1 = 'caracteristicsReg.csv'
url11 = 'caracteristicsRegTest.csv'
urlP = 'pca.csv'
urlPT = 'pcaT.csv'
def Regression():
	X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
	XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
	X_train=X[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_train=X['chance']
	X_test=XT[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
	Y_test=XT['chance']
	#reg = linear_model.LinearRegression()	#0.022112666330325707
	#reg = linear_model.BayesianRidge()		#0.022112934511271203
	#reg = svm.SVR(gamma='scale')			#0.004849921086918859
	reg = MLPRegressor(activation='logistic')#0.0003363074218161884
	reg.fit(X_train,Y_train)
	Z=reg.predict(X_test)
	pd_data = pd.DataFrame(Z,columns=['chance'])
	print(pd_data)
	pd_data.to_csv(urlT,encoding="LATIN_1",index=False)
	joblib.dump(reg,'Regression.model')
	print(mean_squared_error(Y_test,pd_data))
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
Regression()