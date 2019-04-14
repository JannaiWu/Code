class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root=TreeNode(pre[0])#定义根节点
        position=tin.index(root.val)#检索根节点在中序遍历里的位置
        root.left=self.reConstructBinaryTree(pre[1:position+1],tin[0:position])
        #左子树等于递归调用该函数，传入的参数为左子树的前序遍历与中序遍历
        root.right=self.reConstructBinaryTree(pre[position+1:],tin[position+1:])
        #右子树等于递归调用该函数，传入的参数为右子树的前序遍历与中序遍历
        return root

#本题中掌握两个知识点，一个是序列类型的切片[i:j:k]返回的是从i开始，j结束（！不包含j），步长为k的子序列
#类中函数要调用自身的函数需要对self对象进行.fun()操作才能调用，self类似于C++中的this
