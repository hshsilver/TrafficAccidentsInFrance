# coding: utf-8

import pandas as pd
url = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//target.csv'
urlReal = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//targetReal.csv'
url1 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristics.csv'
url3 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//users.csv'
url11 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//caracteristicsTest.csv'
url33 = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//usersTest.csv'
urlP = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//pca.csv'
urlPT = 'C://Users//liuyang//Desktop//France//TrafficAccidentsInFrance//MachineLearing//pcaT.csv'
df = pd.read_csv(url11,encoding="LATIN_1",low_memory=False)#iso8859_15
df1 = pd.read_csv(url33,encoding="LATIN_1",low_memory=False)#iso8859_15
#print(df['long'].dtype)
#df=df.drop('unscathed',axis=1)
#df=df.drop('killed',axis=1)
#df=df.drop('hospital',axis=1)
#df=df.drop('light',axis=1)
#df=df.fillna(0)
#df1=df1.fillna(0)
#df=df.astype('int64')
#df1=df1.astype('int64')
#df=df[~df['long'].isin([0])]
#df['lat']=df['lat'].fillna('null') #将df中A列所有空值赋值为'null'
#df=df[~df['lat'].isin([4])]
#df=df[~df['lat'].isin(['null'])]
#df=df.drop('occutc',axis=1)
#df=df.drop('pr1',axis=1)
#df1['Num_Acc']
#df=df.fillna(0)
#df1=df1.fillna(0)
#df1=df1[df1['Num_Acc'].isin(df['Num_Acc'])]
#df['long']=abs(df['long'])
#df=df.assign(unscathed=0)
df=df.assign(killed=0)
#df=df.assign(hospital=0)
#df=df.assign(light=0)
#df = pd.DataFrame(columns=('unscathed','killed','hospital','light'))
for index in range(len(df1)):#Count the number of people with different degrees of injury
	#print(index)
	if df1.at[index,'grav']==2:
		num = df[df.Num_Acc==df1.at[index,'Num_Acc']].index
		print(num[0])
		df.at[num[0],'killed'] = 1
#print(df.head())
#list=df.values.tolist()
#print(list)
#list=df[['unscathed','killed','hospital','light']]
#print(list.head())
#list.to_csv(url,encoding="LATIN_1",index=False)
df.to_csv(url11,encoding="LATIN_1",index=False)
#df1.to_csv(url22,encoding="LATIN_1",index=False)
