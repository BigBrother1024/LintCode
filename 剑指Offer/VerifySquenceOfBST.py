#思路：
#已知条件：后序序列最后一个值为root；二叉搜索树左子树值都比root小，右子树值都比root大。
#1、确定root；
#2、遍历序列（除去root结点），找到第一个大于root的位置，则该位置左边为左子树，右边为右子树；
#3、遍历右子树，若发现有小于root的值，则直接返回false；
#4、分别判断左子树和右子树是否仍是二叉搜索树（即递归步骤1、2、3）。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        l = len(sequence)
        if l == 0:
            return False
        if l == 1:
            return True
        root = sequence[-1]
        left = 0
        while sequence[left] < root:
            left += 1
        for i in range(left, l):
            if sequence[i] < root:
                return False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:l-1])
