#从尾到头打印链表
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        ls=[]#定义一个反转后的链表
        p=listNode#记录listNode的头指针
        while(p):
            ls.insert(0,p.val)
            p=p.next
        return ls
