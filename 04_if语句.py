"""
 Python的控制流 语句
 1、顺序结构
 2、条件分支语句
 3、循环结构
"""
# 1.顺序结构 就是python从上到下执行代码
# 2.条件分支语句 if: 条件1 elif:条件2 else:条件3
a = 10
b = 1

if a > 11:
    print(a)
elif b == 1:
    print('b等于1')
else:
    print('if语句成功运行了')

'''
 2、循环结构  1、while(): 条件判断   
            2、for循环  遍历列表
while():
  print('hello')
'''
a = 0
# 判断条件是否为真 不为真就会进入死循环
while(a < 10):
    print('hello')
    a += 1
c = {'李神', '123', '456'}
for i in c:
    print(i)
# for 进行常规循环
for i in range(0,6):
     print ('hello world')
'''
     中断结构 break 和 continue
       直接中断程序
      break 直接中断整个循环
      continue 中断一次循环，继续下去循环
'''
a = ['hello1','hello2',3,'world']
for i in a:
        # continue
      print(i)
