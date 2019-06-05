class Solution:
    def __init__(self):
        self.all=[]

    def Permutation(self, ss):
        # write code here
        if len(ss)==0:
            return self.all;
        else:
            self.listall(ss,"") #递归实现字符串的全排列
            result=list(set(self.all)) #这里使用set函数可以去除列表中的重复元素
            return sorted(result) #这里使用sorted函数可以返回一个对列表的元素进行排序后的列表，注意区别与sort函数

    def listall(self,ss,before):
        if not ss: #递归至需要递归的字符串的字符长度为0的时候停止
            self.all.append(before) #向结果列表中增加至此的所有排列组合
        else:
            for i in range(len(ss)):
                self.listall(ss[:i]+ss[i+1:],before+ss[i]) #对于每一个字符串去掉第i个位置的字符，与之前去掉的所有字符形成一个全排列
                #注意python中字符串的切割，s[m,n]是从m开始到n结束（不包括m）的字符串

'''使用itertools库中排列组合函数的方法
import itertools

class Solution:

    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        all=[]
        for i in itertools.permutations(ss):
            if ''.join(i) not in all: #需要将迭代器中的所有字符拼接成一个字符串
                all.append(''.join(i))
        return all
'''
