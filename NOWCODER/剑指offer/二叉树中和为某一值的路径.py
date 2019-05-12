# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def __init__(self):
        #记录结果的二维数组与记录路径的一维数组
        self.result=[]
        self.path=[]

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root or root.val>expectNumber:
            return self.result
        self.findsinglepath(root,expectNumber)
        return self.result


    def findsinglepath(self,root,sum):
        if not root:
            return self.result
        #记录当前节点
        self.path.append(root.val)
        #将sum减去目前添加的root的值
        sum-=root.val
        #如果该节点的左右子树都为空，判断路径的加和是不是等于结果
        if not root.left and not root.right:
            if sum==0:
                self.result.append(self.path[:])
        #递归调用左右子树的查询结果
        if root.left:
            self.findsinglepath(root.left,sum)
        if root.right:
            self.findsinglepath(root.right,sum)
        #左右子树都查找完pop根节点
        self.path.pop()
        return self.result
