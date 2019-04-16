class Solution:
    def minNumberInRotateArray(self, rotateArray):
		if(len(rotateArray)==0):return 0
		else:
			for i in range(len(rotateArray)):
				if(rotateArray[i]>rotateArray[i+1]):
					return rotateArray[i+1]
