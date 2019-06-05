from functools import cmp_to_key

class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        ls=list(map(str,numbers))
        #由于排序中需要使用+的操作将字符串进行连接，因此在此使用map函数，将numbers数字数组转换为字符串数组，然后使用list形成一个列表
        res=sorted(ls,key=cmp_to_key(self.compare))
        #对于python3的版本，sorted的自定义排序方法需要自己写，同时，需要使用functools库中的cmp_to_key函数将比较方法转化为关键key
        s=""
        for i in res:
           s=s+i
        return s

    #比较方法为比较两个字符串连接形成的两个字符串的大小，按照大小进行排序
    def compare(self,a,b):
        if a+b<b+a:
            return -1
        else:
            return 1
