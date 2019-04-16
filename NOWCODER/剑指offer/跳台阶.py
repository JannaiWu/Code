class Solution:
	def jumpFloor(self, n):
		jp1=1 #跳一个台阶有一种跳法
		jp2=2 #跳两个台阶有两种跳法，11，2
		if(n==1):
			return jp1
		if(n==2):
			return jp2
        #跳n个台阶的跳法个数为 n-1个台阶的跳法个数 再跳一阶，或者n-2个台阶的跳法个数直接跳2阶
		for i in range(n-2):
			jp=jp1+jp2
			jp1=jp2
			jp2=jp
		return jp
