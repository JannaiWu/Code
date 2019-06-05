class Solution:
    def FindGreatestSumOfSubArray(self, array):
         sum=0
         max=array[0]
         for i in range(len(array)):
             sum+=array[i]
             if(sum>max):
                 max=sum
             if array[i]>max:
                 sum=array[i]
                 max=sum
         return max
