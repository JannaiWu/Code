class Solution:
	def Fibonacci(self, n):
		fi2=0
		fi1=1
		if(n==0):
			return fi2
		if(n==1):
			return fi1
		for i in range(n-1):
			fb=fi1+fi2
			fi2=fi1
			fi1=fb
		return fb
