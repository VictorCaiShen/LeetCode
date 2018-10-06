class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out_list = []
        self.recrusion('', out_list, n, n)
        return out_list

    def recrusion(self, s, out_list, left, right):
        if left == right == 0:
            out_list.append(s)
        if left > 0:
            self.recrusion(s+'(', out_list, left-1, right)
        if right > left:
            self.recrusion(s+')', out_list, left, right-1)

if __name__ == '__main__':
    s1 = Solution()
    print(s1.generateParenthesis(3))
