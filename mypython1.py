# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来


def run(str1, l):
    if l == 0:
        return
    print(str1[l-1])
    run(str1, l-1)


str1 = input('请输入你要反序的字符')
l = len(str1)

run(str1, l)
