class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        n=len(matrix)
        m=len(matrix[0])
        ls=[]
        up,down,left,right=0,n,0,m#定义好四个边界
        while(True):
            #分为四个步骤，右下左上，打印的过程中，如果遇到边界重合，表示打印完毕，退出循环
            #向右打印，打印完一行，上边界向下移动一个位置
            i=up
            for j in range(left,right,1):
                ls.append(matrix[i][j])
            up+=1
            if(up==down):
                break
            #向下打印，打印完一列，右边界向左移动一个位置
            j=right-1
            for i in range(up,down,1):
                ls.append(matrix[i][j])
            right-=1
            if(right==left):
                break
            #向左打印，打印完一行，下边界向上移动一个位置
            i=down-1
            for j in range(right-1,left-1,-1):
                ls.append(matrix[i][j])
            down-=1
            if(up==down):
                break
            #向上打印，打印完一列，左边界向右移动一个位置
            j=left
            for i in range(down-1,up-1,-1):
                ls.append(matrix[i][j])
            left+=1
            if(right==left):
                break
        return ls
