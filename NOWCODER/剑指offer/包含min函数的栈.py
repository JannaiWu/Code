class Solution:
    def __init__(self):
        self.stack=[]
        self.minstack=[]#定义存储最小值的辅助堆栈
    def push(self, node):
        self.stack.append(node)
        if not self.minstack:#如果辅助栈没有元素直接将node元素push进去
            self.minstack.append(node)
        else:#如果有元素，需要比较node元素与辅助栈的顶元素的大小进行push
            if node<self.minstack[-1]:#如果追加的元素小于栈顶的元素，辅助堆栈的栈顶push该元素
                self.minstack.append(node)
            else:#如果追加的元素大于栈顶的元素，辅助堆栈的栈顶push堆栈栈顶的元素
                self.minstack.append(self.minstack[-1])
    def pop(self):
        if self.stack:#辅助堆栈与元素堆栈同时pop
            self.minstack.pop()
            return self.stack.pop()
        else:
            return None
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minstack[-1]
