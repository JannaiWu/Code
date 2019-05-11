# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        ls=[]
        temp=[]
        if not root:#如果根节点为空，直接返会空
            return []
        temp.append(root)#把根节点放进去
        while temp:
            #temp不空的时候，想把首元素的左右子树放进去(如果存在)
            if temp[0].left:
                temp.append(temp[0].left)
            if temp[0].right:
                temp.append(temp[0].right)
            ls.append(temp.pop(0).val)#向ls中添加每一次弹出的节点的值
        return ls
