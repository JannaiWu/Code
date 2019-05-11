class Solution:
    def IsPopOrder(self, pushV, popV):
        temp=[]
        while 1:
            if not popV:#popV一旦为空退出循环
                break
            if temp and temp[-1]==popV[0]:#如果temp不空且末元素等于popV首元素，同时弹出这两个元素
                temp.pop()
                popV.pop(0)
            elif temp and not pushV and temp[-1]!=popV[0]:#如果temp不空且pushV已空且末元素不等，表示不是正确的出栈顺序
                return False
            else:#其他情况继续进行压栈操作
                temp.append(pushV.pop(0))
        return True
