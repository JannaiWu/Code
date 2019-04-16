class Solution:
    def rectCover(self, n):
        if(n==0):
            return 0
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else:
            re1=2
            re2=1
            for i in range(n-2):
               re=re1+re2
               re2=re1
               re1=re
            return re
