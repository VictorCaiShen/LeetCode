s = '+123213123'
s.strip()
list_num = [str(i) for i in range(0, 10)]
list_sort = []

if s == '' or '+':
    print(s)
else:
    for i in range(0, len(s)):
            if s[i] == '-':
                if i == 0:
                    list_sort.append(s[0])
                else:
                    continue

            elif s[i] in list_num:
                list_sort.append(s[i])

    a = ''.join(list_sort)
    a = int(a)

    if a not in range(-2**31, 2**31):
        if a < 0:
            print(-2**31)
        else:
            print(2**31 - 1)
    else:
        print(a)
