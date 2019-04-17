class Solution:
    def NumberOf1(self, n):
        if(n==0):
            return 0
        if(n<0):
            n+=2**32#对于小于0的数 计算其补数
        s=bin(n)
        s=s.strip("0b")
        return s.count("1")

# 还看到一种算法,可以计算n的二进制数中1的个数
# count=0
# while(n):
#     count+=1
#     n=n&(n-1)
