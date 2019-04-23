class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        cont=0
        p=head
        while(p):
            cont+=1
            p=p.next
        if(k>cont):
            return None
        p=head
        for i in range(cont-k):
            p=p.next
        return p
