bills = [5, 5, 10, 20]
count_5 = 0
count_10 = 0
flag = 0

for i in range(0, len(bills)):
    if bills[i] - 5 == 0:
        count_5 += 1
        flag += 1
    elif bills[i] - 5 == 5:
        if count_5 > 0:
            count_5 -= 1
            count_10 += 1
            flag += 1
        else:
            print(False)
            break

    elif bills[i] - 5 == 15:
        if count_10 > 0 and count_5 > 0:
            count_10 -= 1
            count_5 -= 1
            flag += 1
        elif count_5 >= 3 and count_10 == 0:
            count_5 -= 3
            flag += 1
        else:
            print(False)
            break
if flag == len(bills):
    print(True)
