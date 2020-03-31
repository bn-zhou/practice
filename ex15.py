# -- coding: utf-8 -- 。
#从sys(模组/库)中导入(import)argv参数
from sys import argv
     #将参数argv解包
script, filename = argv


#指定打开一个文件
txt = open(filename)



#打印文件名
print ("Here's your file %r:" %filename)
#打印文件内容
print (txt.read())

print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())

