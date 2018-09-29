class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_list = []
        dit = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv ',
            '9': 'wxyz',
        }
        digits = list(digits)
        while digits:
            a = digits.pop(0)
            if num_list == []:
                for i in dit[a]:
                    num_list.append(i)
            else:
                num_list2 = []
                for i in dit[a]:
                    def add_f(n):
                        return n + i
                    num_list2 += list(map(add_f, num_list))
                num_list = num_list2

        return num_list

if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations('237'))