class Solution:
    def jumpFloorII(self,n):
        if(n==1):
            return 1
        elif(n==2):
            return 2
        else :
            jp=0
            for i in range(1,n):
                jp=jp+self.jumpFloorII(i)
            jp+=1
            return jp
