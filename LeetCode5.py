class Solution:
    def longestPalindrome(self, s):
        a = int(len(s))
        dit = {}
        if a == 1 or a == 0:
            return s
        else:
            for i in range(0, a):
                for j in range(i+1, a+1):
                    if self.check_echo(s[i:j]):
                        dit[s[i:j]] = j-i
        if dit != {}:
            return max(dit, key=dit.get)

    def check_echo(self, str_1):
        str_2 = list(reversed(str_1))
        if list(str_1) == list(str_2):
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('bb'))