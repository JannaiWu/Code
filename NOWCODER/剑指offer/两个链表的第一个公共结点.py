class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        #将两个链表的所有节点放在两个栈里
        l1=0
        s1=[]
        while pHead1:
            l1+=1
            s1.append(pHead1)
            pHead1=pHead1.next
        l2=0
        s2=[]
        while pHead2:
            l2+=1
            s2.append(pHead2)
            pHead2=pHead2.next
        #从尾部开始找，因为一旦产生公共节点，后面的所有元素都相同，找到最后一个相同的节点即可
        res=None
        while len(s1)!=0 and len(s2)!=0:
            v1=s1.pop()
            v2=s2.pop()
            if v1==v2:
                res=v1
                continue
            else:
                break
        return res
