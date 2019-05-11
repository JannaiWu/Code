class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        else:
            return self.judge(sequence)

    def judge(self,seq):
        if not seq:
            return True
        elif len(seq)==1 or len(seq)==2:#如果只有一个元素或者两个元素，证明一定是后序遍历
            return True
        else:
            leftroot=-1
            rightroot=len(seq)-2#找到右子树的根节点
            for i in range(1,len(seq),1):
                if(seq[i]>seq[-1] and seq[i-1]<seq[i]):
                    leftroot=i-1#找到左子树的根点
                    break
            #判断是否是合法的右子树节点
            if(seq[rightroot]<seq[-1]):#如果不存在右子树
                rightroot=-1
            #首先判断左右子树是不是都满足左树小于根节点，右树大于根节点
            judge1=True
            judge2=True
            #判断左右子树内所有元素是否合法
            for i in range(0,leftroot+1,1):
                judge1=judge1 and seq[i]<seq[-1]
            for i in range(leftroot+1,rightroot+1,1):
                judge2=judge2 and seq[i]>seq[-1]
            #返回是否合法结果以及递归左右子树是否合法
            return judge1 and judge2 and self.judge(seq[0:leftroot+1]) and self.judge(seq[leftroot+1:rightroot+1])
