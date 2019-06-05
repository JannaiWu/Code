class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ones=0
        mul=1
        store=n #储存n的值，用于对某一高位的第一位为1的情况进行计算
        while(n!=0):
            tmp=n//10 #临时储存n的高位数字
            #根据当前低位的首位三种情况分别进行计算
            if n%10==0:
                ones+=tmp*mul
            elif n%10==1:
                ones+=tmp*mul
                ones+=store%mul+1
            else:
                ones+=(tmp+1)*mul
            n=n//10
            mul*=10
        return ones
