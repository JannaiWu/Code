class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput.sort() #使用sort函数对数组进行排序
        if k>len(tinput): #对于k大于数组长度的情况 直接返回空的数组
            return []
        return tinput[:k]
