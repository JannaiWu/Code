# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#使用计算左右子树的方法，来判断是否是一个平衡二叉树，时间复杂度是n^2的
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return False
        #计算左右树的高度需要进行一次递归，时间复杂度为n
        leftdepth=self.TreeDepth(pRoot.left)
        rightdepth=self.TreeDepth(pRoot.right)
        if abs(leftdepth-rightdepth)<=1:
            flag=True
        else:
            flag=False
        #每个节点要重复调用自己的判断函数，时间复杂度为n，因此总的时间复杂度为n^2
        return flag and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        #调用上一题写的计算一个二叉树深度的函数
        if not pRoot:
            return 0
        else:
            return max(1+self.TreeDepth(pRoot.left),1+self.TreeDepth(pRoot.right))

#这种解法的时间复杂度降到n，原因是每次遍历，如果不符合高度要求，直接返回-1
class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.helper(pRoot)!=-1

    #定义辅助函数，只要某一个树的值设为-1，证明该树中有不平衡二叉树，这个树以上的所有树都为不平衡二叉树
    def helper(self,pRoot):
        if not pRoot:
            return 0
        left=self.helper(pRoot.left)
        if left==-1:
            return -1
        right=self.helper(pRoot.right)
        if right==-1:
            return -1
        #如果两个树都没有不平衡二叉树，需要判断左右树的高度差是否<1，如果不小于1，需要返回该树的高度
        if abs(left-right)>1:
            return -1
        return 1+max(left,right)
