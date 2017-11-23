#coding:utf-8
import random


#开奖结果
def getResult():
	red=random.sample(range(1,33),6)
	green=random.sample(range(1,16),1)[0]
	return red,green
#中奖条件
winnerCondition={
	'一等奖':{
		'red':6,
		'green':True,
		'money':10000000
	},
	'二等奖':{
		'red':6,
		'green':False,
		'money':5000000
	},
	'三等奖':{
		'red':5,
		'green':True,
		'money':300000
	},
	'四等奖':{
		'red':5,
		'green':False,
		'money':20000
	},
	'四等奖':{
		'red':4,
		'green':True,
		'money':20000
	},
	'五等奖':{
		'red':4,
		'green':False,
		'money':100
	},
	'五等奖':{
		'red':3,
		'green':True,
		'money':100
	},
	'六等奖':{
		'red':2,
		'green':True,
		'money':5
	},
	'六等奖':{
		'red':1,
		'green':True,
		'money':5
	},
	'六等奖':{
		'red':0,
		'green':True,
		'money':5
	}
}
#查看中奖结果
def lucklyResult(selectRed,selectGreen):
	red,green=getResult()
	luckly_red=[ item for item in selectRed if item in red]
	luckly_green=True if green==selectGreen else False
	for key,value in winnerCondition.items():
		if len(luckly_red)==int(value['red']) and luckly_green==value['green']:
			return key,value['money'],red,green

#开始投注
def cathectic():
	#我的投注,看看循环n次能中多少次
	selectRed=[21, 16, 18, 20, 13, 15]
	selectGreen=5
	result=lucklyResult(selectRed,selectGreen)

	if result:
		print '开奖号码为:{0}:{1}'.format(result[2],result[3])
		print '中奖结果为:{0},获得奖金为:{1}!'.format(result[0],result[1])
	else:
		print '很遗憾,您没有中奖!'

for i in range(1,10000):
	result=cathectic()