class Solution:
    def InversePairs(self, data):
        return self.cal(0,len(data)-1,data)%1000000007

    def cal(self,left,right,data):
        #递归终止条件
        if right-left==0:
            return 0
        if right-left==1:
            if data[right]<data[left]:
                data[left],data[right]=data[right],data[left]
                return 1
            else:
                return 0
        mid=(left+right)//2
        res=self.cal(left,mid,data)+self.cal(mid+1,right,data)
        res%=1000000007

        #计算左右两个有序序列产生的逆序对个数
        #需要定义一个指针指向右边有序序列的最后一个元素
        pr=right
        for i in range(mid,left-1,-1): #对左边的有序序列，比较其与右边pr所指的元素的大小关系
            while(data[i]<data[pr] and pr!=mid):#如果右边比左边大，右边的指针左移动，直至找到右边第一个比左边该数小的数字
                pr-=1
            res+=pr-mid #这样对于左边这个数字就会产生pr-mid个逆序
            res%=1000000007

        #将两个数组归并后传入原来的data中
        pl=left
        pr=mid+1
        temp=[]
        #第一步使用三个while循环，将两个有序数列归并成一个有序序列
        while pl!=mid+1 and pr!=right+1:
            if data[pl]<data[pr]:
                temp.append(data[pl])
                pl+=1
            else:
                temp.append(data[pr])
                pr+=1
        while pl!=mid+1:
            temp.append(data[pl])
            pl+=1
        while pr!=right+1:
            temp.append(data[pr])
            pr+=1
        #第二步使用一个for循环将原始的data从left到right的数字替换为上面的有序序列
        p=0
        for i in range(left,right+1):
            data[i]=temp[p]
            p+=1
        return res%1000000007
