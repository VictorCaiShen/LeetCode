class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        else:
            if needle in haystack:
                for i in range(len(haystack)):
                    if haystack[i:i+len(needle)] == needle:
                        return i
            else:
                return -1

if __name__ == "__main__":
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack,needle))