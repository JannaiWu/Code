class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        newhead=None
        #需要注意三个指针的替换顺序 不要访问到未知的区域了
        while(pHead):
            tep=pHead.next
            pHead.next=newhead
            newhead=pHead
            pHead=tep
        return newhead
