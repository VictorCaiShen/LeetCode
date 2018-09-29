class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dit = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000,
        }
        sums = 0
        lists = list(map(str, str(s)))
        print(lists)
        for i in range(0, len(lists)):
            if i < len(lists) - 1:
                seq = [lists[i], lists[i + 1]]
                seq1 = ''.join(seq)
            if seq1 in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                i += 1
                sums += dit[seq1]
            else:
                sums += dit[lists[i]]
        return sums