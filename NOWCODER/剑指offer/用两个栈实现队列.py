# -*- coding:utf-8 -*-
class Solution:
    #对该类进行初始化
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        #在这里对self的所有成员进行定义
        #初始化函数不能return

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack1 and not self.stack2:#如果两个栈都为空，则返回空
            return []
        elif not self.stack2 :#如果仅仅第二个栈为空，将第一个栈的元素弹到第二个栈
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()
