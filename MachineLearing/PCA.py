# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
url = 'target.csv'
urlReal = 'targetReal.csv'
url1 = 'caracteristics.csv'
url3 = 'users.csv'
url11 = 'caracteristicsTest.csv'
url33 = 'usersTest.csv'
urlP = 'pca.csv'
urlPT = 'pcaT.csv'
num = 6
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
pcT.to_csv(urlPT,encoding="LATIN_1",index=False)