# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
url1 = 'caracteristics.csv'
df = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
X = df
X_train=X[['lum', 'int', 'atm','col','lat','long', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]
Y_train=X[['unscathed', 'killed', 'hospital', 'light']]
fig = plt.figure('LDA')
lda = LinearDiscriminantAnalysis(n_components=3)
lda.fit(X_train,Y_train['killed'])
X_new = lda.transform(X_train)
print("The ratio of the variance value to the total variance of each principal component after dimensionality reduction:",lda.explained_variance_ratio_)
print("Sample size and dimensions before dimension reduction:",X_train.shape)
print("Sample size and dimensions after dimensionality reduction:",X_new.shape)
plt.scatter(X_new[:, 0],X_new[:, 1],X_new[:, 2],marker='o',c=Y_train['killed'],alpha=0.5)

plt.show()