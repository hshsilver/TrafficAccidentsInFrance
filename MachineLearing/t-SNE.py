# coding: utf-8

from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
url1 = 'caracteristicsTest.csv'
df = pd.read_csv(url1,encoding="LATIN_1",low_memory=False)#iso8859_15
X = df[['lum', 'int', 'atm','col', 'catr', 'circ', 'nbv', 'vosp','prof', 'plan', 'lartpc', 'larrout', 'surf', 'infra', 'situ', 'env1']]

tsne=TSNE()
print("111")
tsne.fit_transform(X)  #进行数据降维,降成两维
print("222")
#a=tsne.fit_transform(data_zs) #a是一个array,a相当于下面的tsne_embedding_
tsne=pd.DataFrame(tsne.embedding_,index=X.index) #转换数据格式
print("333")

d=tsne[r[u'聚类类别']==0]
plt.plot(d[0],d[1],'r.')

d=tsne[r[u'聚类类别']==1]
plt.plot(d[0],d[1],'go')

d=tsne[r[u'聚类类别']==2]
plt.plot(d[0],d[1],'b*')

plt.show()
