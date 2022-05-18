# python 变量  标示符 有字母、下划线、数字组成
 # 不能以数字开头 且不能跟关键字同名

# 关键字  Python已经定义好的
  # 具有特殊的功能和含义 不允许定义跟关键字相同的关键字
# import keyword 导入 关键字  模块
# 模块  相当于工具包 keyword
import keyword
print(keyword.kwlist)  # Python已经 定义好关键字

"""
    给变量起名的 时候 
       标示符 区分大小写 Curry 和 curry 是2个不一样的变量
         各保留一个空格 name = 'lishen'
           每个单词都使用 小写字母 和_下划线连接
            frist_name, last_name qq_number 

驼峰命名法
   大驼峰和小驼峰 命名
     第一个字母大写或者小写 例如: FristName,lastName, 2个单词都大写
     小驼峰 userName,lastName 第一字母单子小写 第二个大写
     
"""