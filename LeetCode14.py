class Solution:
    def longestCommonPrefix(self, s1):
        """
        :type strs: List[str]
        :rtype: str
        """
        if '' in s1 or s1 == []:
            return ''
        elif len(s1) == 1:
            return s1[0]
        else:
            min_len1 = min(len(s) for s in s1)
            flag = 0
            for j in range(min_len1):
                for i in range(len(s1)-1):
                    if s1[i][j] == s1[i+1][j]:
                        if i == len(s1)-2 and flag >= j:
                            flag += 1
                    else:
                        break
            if flag > 0:
                return s1[0][:flag]
            else:
                return ""

if __name__ == "__main__":
    a = Solution()
    s1 = ["aca", "aba"]
    print(a.longestCommonPrefix(s1))
