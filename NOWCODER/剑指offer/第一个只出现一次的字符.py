class Solution:
    def FirstNotRepeatingChar(self, s):
        cnt=[]
        for i in range(123):
            cnt.append(0)
        for ss in s:
            cnt[ord(ss)]+=1
        for i in range(len(s)):
            if cnt[ord(s[i])]==1:
                return i
        return -1

#网上高手的方法
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        cal=lambda c:s.count(c)==1
        ls=list(filter(cal,s))
        return s.index(ls[0])
'''
