# 乘法口诀的程序
# end = " " 不换行输出
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '='+str(i*j), end="   ")
        print()
