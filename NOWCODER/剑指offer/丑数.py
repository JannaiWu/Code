class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<7:
            return index
        ls=[1]
        p2,p3,p5=0,0,0
        for i in range(index-1):
            #找下一个丑数
            nextuglyn=min(ls[p2]*2,min(ls[p3]*3,ls[p5]*5))
            ls.append(nextuglyn)
            if(nextuglyn==ls[p2]*2):
                p2+=1
            if(nextuglyn==ls[p3]*3):
                p3+=1
            if(nextuglyn==ls[p5]*5):
                p5+=1
        return ls[index-1]
