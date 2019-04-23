class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1 and pHead2:
            return pHead2
        elif not pHead2 and pHead1:
            return pHead1
        elif not pHead1 and not pHead2:
            return None
        else:
            newhead=None
            if(pHead1.val<pHead2.val):
                newhead=pHead1
                pHead1=pHead1.next
            else:
                newhead=pHead2
                pHead2=pHead2.next
            start=newhead
            #标记了头结点的位置
            while(pHead1 and pHead2):#当原始两个链表均不为空的时候，循环执行，一旦有一个链表为空则退出
                if(pHead1.val<pHead2.val):
                    newhead.next=pHead1
                    pHead1=pHead1.next
                else:
                    newhead.next=pHead2
                    pHead2=pHead2.next
                newhead=newhead.next
            #将最后没有附加的节点放在新链表的最后
            if not pHead1:
                newhead.next=pHead2
            else:
                newhead.next=pHead1
            return start#返回新链表的头指针
