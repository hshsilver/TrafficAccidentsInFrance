# coding: utf-8
import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt

url1 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristics.csv'
url = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//target.csv'
urlReal = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//targetReal.csv'
urlT = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//targetTest.csv'
url11 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristicsTest.csv'
X = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
Y = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
XT = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
X_train=X[['lum', 'agg', 'int', 'atm','col', 'lat', 'long', 'catr', 'circ', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1', 'killed']]
#X_test=XT[['lum', 'agg', 'int', 'atm','col', 'lat', 'long', 'catr', 'circ', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1', 'killed']]
k_means = cluster.KMeans(n_clusters=5)
y_pred = k_means.fit_predict(X_train)

fig = plt.figure()
ax = fig.add_subplot(2, 2, 1)
ax.scatter((X_train.values)[:,5], (X_train.values)[:,6], c=y_pred)
ax.set_xlabel("lat")
ax.set_ylabel("long")
ax.set_title("K-means")
ax.legend(framealpha=0.5)

'''
ax1 = fig.add_subplot(2, 2, 2)
ax1.scatter((X_train.values)[:,12], (X_train.values)[:,13], c=y_pred)
ax1.set_xlabel("lartpc")
ax1.set_ylabel("larrout")
ax1.set_title("K-means")
ax1.legend(framealpha=0.5)

ax2 = fig.add_subplot(2, 2, 3)
ax2.scatter((X_train.values)[:,12], (X_train.values)[:,18], c=y_pred)
ax2.set_xlabel("lartpc")
ax2.set_ylabel("killed")
ax2.set_title("K-means")
ax2.legend(framealpha=0.5)

ax3 = fig.add_subplot(2, 2, 4)
ax3.scatter((X_train.values)[:,5], (X_train.values)[:,18], c=y_pred)
ax3.set_xlabel("lat")
ax3.set_ylabel("killed")
ax3.set_title("K-means")
ax3.legend(framealpha=0.5)
'''
plt.show()