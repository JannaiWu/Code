# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #定义mid数组来储存中序遍历结果，对于二叉搜索树，中序遍历结果就是有序的序列
    def __init__(self):
        self.mid=[]

    #转换函数将按照中序的序列结果，将后一节点的左树设为前一节点，前一节点的右树设为后一节点
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        self.inorder(pRootOfTree)
        for i in range(len(self.mid)-1):
            self.mid[i].right=self.mid[i+1]
            self.mid[i+1].left=self.mid[i]
        return self.mid[0]

    #将中序遍历的结果放在mid数组中
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        self.mid.append(root)
        self.inorder(root.right)
        return
