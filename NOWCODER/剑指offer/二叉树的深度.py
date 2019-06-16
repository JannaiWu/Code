# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#使用递归的方法写的，左右分别递归调用
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        else:
            return max(1+self.TreeDepth(pRoot.left),1+self.TreeDepth(pRoot.right))

#使用层次遍历的方法，用队列储存每一层的内容
class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        depth=0
        store=[]
        #将根节点放在队列中
        store.append(pRoot)
        while(len(store)!=0):
            #首先记录本层的节点个数
            thislevel=len(store)
            #依次将本次每个节点的左右节点放在队列中
            for i in range(thislevel):
                if store[i].left:
                    store.append(store[i].left)
                if store[i].right:
                    store.append(store[i].right)
            #将本层的每个节点移除
            for i in range(thislevel):
                store.pop(0)
            #遍历一遍层数加1
            depth+=1
        return depth
