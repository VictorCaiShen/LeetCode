s = input()
length = 1
temp = 0

null_1 = 0


for i in range(0, len(s)-2):
    for j in range(0, len(s)-1):
        if s[j] != s[j+1]:
            length += 1
        else:
            if length > null_1:
                null_1 = length
                length = 0
                break
            else:
                break
print(null_1)

