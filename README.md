## 模拟双色球投注、开奖、中奖全过程

## 安装方法
```
git clone 
```
## 运行
```
cd luckboy
python luckboy.py
```
##程序默认一组投注，你也可以改成你自己的投注，也可以增加投注次数，我投了100万次才中的一个二等奖，看来彩票不能玩啊，逃！
```
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
#默认循环10000次开奖结果
for i in range(1,10000):
	result=cathectic()
```