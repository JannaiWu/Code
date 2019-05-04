# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 由于题目要求将源二叉树变化为镜像，因此不能新建一个二叉树
        if root==None:
            return
        root.left,root.right=root.right,root.left#需要在源二叉树上进行操作，交换左右树
        self.Mirror(root.left)#递归左树
        self.Mirror(root.right)#递归右树
        return
