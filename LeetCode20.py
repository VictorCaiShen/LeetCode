class Solution:
    def isValid(self, s):
        dit = {
            '[' : ']',
            '{': '}',
            '(': ')',
        }
        stack = []
        if not s:
            return True
        for i in s:
            if i in dit:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif dit[stack.pop()] != i:
                    return False
        if stack:
            return False
        else:
            return True

if __name__ == "__main__":
    s1 = Solution()
    s = '[()[]]'
    print(s1.isValid(s))

