class Solution:
    def reOrderArray(self, array):
        ls=[]
        for i in range(len(array)):
            if(array[i]%2==1):
                ls.append(array[i])
        for i in range(len(array)):
            if(array[i]%2==0):
                ls.append(array[i])
        return ls
