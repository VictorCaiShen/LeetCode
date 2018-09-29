s = 'asdwqdwqdwqe'
numRows = 4
if numRows == 1:
    print(s)
zigzag = ['' for i in range(numRows)]  # 初始化zigzag为['','','']
row = 0                                # 当前的行数
step = 1                               # 步数：控制数据的输入
for c in s:
    if row == 0:
        step = 1
    if row == numRows - 1:
        step = -1
    zigzag[row] += c
    row += step
print(''.join(zigzag))