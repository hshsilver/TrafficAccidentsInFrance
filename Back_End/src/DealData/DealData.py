from src.MachineLeaning.MLI import *
import calendar
import json
def getMonthIn4(date):
	year, month = date.split('-')
	jsonMonth = monthDataToObj()
	result = {}
	result['data'] = []
	for i in range(1,calendar.monthrange(int(year),int(month))[1] + 1):
		day = str(year) + '-' + str(month) + '-' + str(i).zfill(2)
		if (day in jsonMonth):
			result['data'].append(jsonMonth[day])
		else:
			result['data'].append([0,0,0,0])
	return json.dumps(str(result))

def monthDataToObj():
	data = showChart(1)
	result = {}
	for item in data:
		result[item[0]] = [item[2],item[3],item[4],item[5]]
	return result

def createAccident(dic):
	num = (dic['year'] + dic['month'] + dic['day'] + dic['time'])
	Num_Acc = int(num)
	year = int(dic['year'])##
	month = int(dic['month'])##
	day = int(dic['day'])##
	time = int(dic['time'])##
	lum = int(dic['lum']) #光照#
	int_ = int(dic['int']) #交叉#
	atm = int(dic['atm']) #天气#
	col = int(dic['col']) #碰撞类型#
	lat = int(float(dic['lat'])*100000) #维度#
	long_ = int(float(dic['long'])*100000) #经度#
	catr = int(dic['catr']) #道路类别#
	circ = int(dic['circ']) #道路类型#
	nbv = int(dic['nbv']) #交通车道总数#
	vosp = int(dic['vosp'])#表示是否存在预留车道，无论该车道是否发生事故#
	prof = int(dic['prof'])#纵向剖面描述了事故现场道路的坡度#
	plan = int(dic['plan'])#路线#
	lartpc = int(dic['lartpc'])#中央实地宽度（TPC），如果有的话#
	larrout = int(dic['larrout'])#分配给车辆交通的道路宽度不包括紧急停止带，心肺复苏术和停车位#
	surf = int(dic['surf'])#表面状况#
	infra = int(dic['infra'])#发展 - 基础设施#
	situ = int(dic['situ'])#事故情况#
	env1 = int(dic['env1'])#学校点：靠近学校#
	acc = Accident(Num_Acc, year, month, day, time, lum, int_, atm, col, lat, long_, catr, circ, nbv, vosp, prof, plan, lartpc, larrout, surf, infra, situ, env1)
	return acc

def saveAccident(dic):
	acc = createAccident(dic)
	injury = [int(dic['unscathed']),int(dic['killed']),int(dic['hospital']),int(dic['light'])]
	upload(acc,injury)
	result = {}
	result['data'] = 'true'
	return json.dumps(result)

def getAllAccident():
	allAcc = showAll()
	result = {}
	result['data'] = []
	for item in allAcc:
		#print(item[2])
		item[2] = int(item[2])
		result['data'].append(item)
	#print(result['data'][0])
	return json.dumps(result)

def getDetail(accNum):
	result = {}
	data = showDetail(accNum)[0]
	data = getDetailInformation(data)
	result['data'] = data
	return json.dumps(result)

def getPredictDeaths(dic):
	acc = createAccident(dic)
	result = {}
	result['data'] = predictDeaths([acc])[0].tolist()
	return json.dumps(result)

def getPredictProbability(dic):
	result = {}
	result['data'] = predictTheProbability()
	return json.dumps(result)

#5 light
#6 int 交叉
#7 atm 天气
#8 col 碰撞类型#
#11 ctar 道路类别
#12 circ 道路类型#
#14 vosp 预留车道
#15 prof 坡度
#16 plan 路线
#19 surf 表面状况#
#20 infra 发展 - 基础设施
#21 situ 事故情况
def getDetailInformation(data):
	data[5] = getLight(data[5])
	data[6] = getInt(data[6])
	data[7] = getAtm(data[7])
	data[8] = getCol(data[8])
	data[11] = getCtar(data[11])
	data[12] = getCirc(data[12])
	data[14] = getVosp(data[14])
	data[15] = getProf(data[15])
	data[16] = getPlan(data[16])
	data[19] = getSurf(data[19])
	data[20] = getInfra(data[20])
	data[21] = getSitu(data[21])
	return data;

def getLight(index):
	theMap = {
		'0':'null',
		'1':'full day',
		'2':'twilight or dawn',
		'3':'night without public lightinglanes',
		'4':'night with public lighting not lit',
		'5':'night with public lighting on'
	}
	return theMap[str(index)]

def getInt(index):
	theMap = {
		'0':'null',
		'1':'out of intersection',
		'2':'intersection in x',
		'3':'intersection in t',
		'4':'intersection in y',
		'5':'intersection with more than 4 branches',
		'6':'gyratory',
		'7':'place',
		'8':'level crossing ',
		'9':'other intersection'
	}
	return theMap[str(index)]

def getAtm(index):
	theMap = {
		'0':'null',
		'1':'normal',
		'2':'light rain',
		'3':'heavy rain',
		'4':'snow - hail',
		'5':'fog - smoke',
		'6':'strong wind - storm',
		'7':'dazzling weather',
		'8':'cloudy weather',
		'9':'other'
	}
	return theMap[str(index)]

def getCol(index):
	theMap = {
		'0':'null',
		'1':'two vehicles - frontal',
		'2':'two vehicles - from the rear',
		'3':'two vehicles - by the side',
		'4':'three vehicles and more - in chain',
		'5':'three or more vehicles - multiple collisions',
		'6':'other collision',
		'7':'without collision',
	}
	return theMap[str(index)]

def getCtar(index):
	theMap = {
		'0':'null',
		'1':'highway',
		'2':'national road',
		'3':'departmental road',
		'4':'communal way',
		'5':'off public network',
		'6':'parking lot open to public traffic',
		'9':'other',
	}
	return theMap[str(index)]

def getCirc(index):
	theMap = {
		'0':'null',
		'1':'one way',
		'2':'bidirectional',
		'3':'separated carriageways',
		'4':'with variable assignment channels',
	}
	return theMap[str(index)]

def getVosp(index):
	theMap = {
		'0':'null',
		'1':'bike path',
		'2':'cycle bank',
		'3':'reserved channel',
	}
	return theMap[str(index)]

def getProf(index):
	theMap = {
		'0':'null',
		'1':'dish',
		'2':'slope',
		'3':'hilltop',
		'4':'hill bottom',
	}
	return theMap[str(index)]

def getPlan(index):
	theMap = {
		'0':'null',
		'1':'straight part',
		'2':'curved on the left',
		'3':'curved right',
		'4':'in "S"',
	}
	return theMap[str(index)]

def getSurf(index):
	theMap = {
		'0':'null',
		'1':'normal',
		'2':'wet',
		'3':'puddles',
		'4':'flooded',
		'5':'snow',
		'6':'mud',
		'7':'icy',
		'8':'fat - oil',
		'9':'other',
	}
	return theMap[str(index)]

def getInfra(index):
	theMap = {
		'0':'null',
		'1':'underground - tunnel',
		'2':'bridge - autopont',
		'3':'exchanger or connection brace',
		'4':'railway',
		'5':'carrefour arranged',
		'6':'pedestrian area',
		'7':'toll zone',
	}
	return theMap[str(index)]

def getSitu(index):
	theMap = {
		'0':'null',
		'1':'on the road',
		'2':'on emergency stop band',
		'3':'on the verge',
		'4':'on the sidewalk',
		'5':'on bike path',
	}
	return theMap[str(index)]

