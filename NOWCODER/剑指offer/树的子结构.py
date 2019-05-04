class Solution:
    def HasSubtree(self, p1, p2):
        if p1==None or p2==None:
            return False
        else:
            return self.judge(p1,p2)
    #由于递归中如果递归到p2为空树，应该返回True，因此需要重新建立一个递归函数
    def judge(self,p1,p2):
        if p2==None:#当p2为空，返回true
            return True
        if p1==None:#当p1为空的时候，p2必须一样为空
            return p1==p2
        result=False
        if p1.val==p2.val:#当p1,p2值一样的时候，开始递归判断p1,p2的左右树
            result=self.judge(p1.left,p2.left) and self.judge(p1.right,p2.right)
        return result or self.judge(p1.left,p2) or self.judge(p1.right,p2)
        #返回result的判断结果，或者在p1的左右树中查找
