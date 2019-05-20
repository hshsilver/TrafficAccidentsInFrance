import numpy as np
import pandas as pd
from sklearn import cluster
import matplotlib.pyplot as plt

url = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//pca.csv'

X = pd.read_csv(url,encoding="LATIN_1",low_memory=False)#iso8859_15
X_train=X
k_means = cluster.KMeans(n_clusters=4)
y_pred = k_means.fit_predict(X_train)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter((X_train.values)[:,0], (X_train.values)[:,1], c=y_pred)
ax.set_xlabel("first eigenvector")
ax.set_ylabel("second eigenvector")
ax.legend(framealpha=0.5)
plt.show()