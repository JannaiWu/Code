class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        store={}
        for i in numbers:
            if i in store: #使用in判断字典中是否含有i的引索元素
                store[i]+=1
            else:
                store[i]=1
            if store[i]>len(numbers)/2: #一旦找到出现次数超过数组长度一般的数字直接return
                return i
        return 0
