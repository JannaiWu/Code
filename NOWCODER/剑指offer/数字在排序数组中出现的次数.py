class Solution:
    def GetNumberOfK(self, data, k):
        count=0
        falg=False
        for i in range(len(data)):
            if data[i]==k:
                count+=1
                falg=True
                continue
            elif not falg:
                continue
            break
        return count
#最普通的遍历方法

#下面是使用二分查找法写的方法，虽然将时间复杂度转化为logn但是在牛客网的提交速度并没有快很多……
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        left=0
        right=len(data)-1
        if not data:
            return 0
        #使用二分查找，找到出现这个数字的位置，下面是标准的二分查找的写法
        while(left<=right):
            mid=(left+right)/2
            if data[mid]==k:
                break
            if data[mid]>k:
                right=mid-1
            elif data[mid]<k:
                left=mid+1
        #如果找到了mid，count先增加1
        if data[mid]==k:
            count=1
        else:
            return 0
        #分别向左向右找到其余的数字
        posl,posr=mid-1,mid+1#找到k的左右位置
        #注意不要超出边界
        while(posl!=-1):
            if data[posl]==k:
                posl-=1
                count+=1
            else:
                break
        while(posr!=len(data)):
            if data[posr]==k:
                posr+=1
                count+=1
            else:
                break
        return count
