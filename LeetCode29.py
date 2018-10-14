class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        temp = 0
        if divisor >= 0 and dividend >= 0 or divisor < 0 and dividend < 0:
            sign = 1
        else:
            sign = -1
        if dividend == 0 or divisor == 0:
            return 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        for i in range(32, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                result |= 1 << i

        if sign < 0:
            result = -result
        elif sign > 0:
            result = result

        if result < -2**31 or result > (2**31) -1:
            return 2**31 -1
        else:
            return result

if __name__ == "__main__":
    s = Solution()
    dividend = 2**31 -1
    divisor = 1
    print(s.divide(dividend,divisor))