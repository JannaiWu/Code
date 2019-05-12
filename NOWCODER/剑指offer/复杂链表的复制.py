# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        newnode=self.cloneonenode(pHead)
        return newnode

    def cloneonenode(self,old):
        #如果该节点为空，返回一个复制的空节点
        if not old:
            return None
        #复制值
        newnode=RandomListNode(old.label)
        #复制下一个节点
        newnode.next=self.cloneonenode(old.next)
        #记录随机指向节点
        newnode.random=old.random
        return newnode


'''class RandomListNode:
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        ptr=pHead
        while ptr:
            #临时储存ptr的下一节点
            tep=ptr.next
            #将ptr的下一节点设为复制的节点
            ptr.next=self.cloneonenode(ptr)
            #复制节点的下一节点设为tep
            ptr.next.next=tep
            #ptr移动到tep上
            ptr=tep
        #以上完成了新旧链表的交替，接下来将所有节点中存在随机指针的新节点调整
        ptr=pHead
        while ptr:
            #如果ptr存在random指针
            if ptr.random:
                ptr.next.random=ptr.random.next
            ptr=ptr.next.next
        #以上将随机指针设置完毕，之后将新旧链表分离
        p1=pHead
        p2=pHead.next#需要将新节点的头指针记录下来
        new=pHead.next
        while True:
            p1.next=p2.next
            p1=p1.next
            if not p1:#一但原链表到头，退出循环
                break
            p2.next=p1.next
            p2=p2.next
        return new

    def cloneonenode(self,old):
        #如果该节点为空，返回一个复制的空节点
        if not old:
            return None
        newnode=RandomListNode(old.label)
        return newnode
'''
