# 打印出四个方向的九九乘法表

# 左上方向
for x in range(1, 10):
    for y in range(1, x+1):
        # %d格式化字符串，%2d占两个位置，end=''不换行
        print('%d*%d=%2d' % (y, x, x*y), end='  ')
    print('')  # 换行
print()

# # 左下方向
for x in range(9, 0, -1):
    for y in range(1, x+1):
        print('%d*%d=%2d' % (y, x, x*y), end='  ')
    print('')
print()

# 右上方向
for x in range(1, 10):
    z = 9 - x
    print(' '*8*z, end='')
    for y in range(1, x+1):
        print('%d*%d=%2d' % (y, x, x*y), end='  ')
    print('')
print()

# 右下方向
for x in range(9, 0, -1):
    z = 9 - x
    print(' '*8*z, end='')
    for y in range(1, x+1):
        print('%d*%d=%2d' % (y, x, x*y), end='  ')
    print('')