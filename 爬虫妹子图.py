import os
import requests
import re
if not os.path.exists('./image'):
    os.mkdir('./image')
# 网址 python的语言 可以使用 中文变量
url  = "https://www.tupianzj.com/meinv/mm/meizitu/"

# import 工具库 requests .content 提取图片数据 提取文件数据 gbk是国标扩展 是专门解码中文的
response = requests.get(url).content.decode('gbk');

# 看一看得到数据
# print(response)

# 提取所有图片的网址  数据筛选 满足留下来  不满足丢了
image_infos = re.findall('<img src="(.*)" alt="(.*)" border=("0") />',response)
# print(image_infos)

# [( 网址1,名字1),(网址2,名字2),……]
for i in image_infos:# 得到了图片网址 下载图片
    print(i,type(i))
    name = i[1]
    print(name)
    image = requests.get(i[0]).content
    #保存图片 放在哪里地方 起个名字
    with open("./image/"+ name + ".jpg","wb") as f:
        f.write(image)
        print(name,'下载完成！！')


