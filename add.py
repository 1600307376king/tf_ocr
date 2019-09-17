import pandas as pd

# f = open('./常用汉字字符串.txt', 'r', encoding='utf-8')
#
#
# s = ' 这个PEP的目的是介绍在一个Python源文件中如何声明编码的语法。随后Python解释器会在解释文件的时候用到这些编码信息。最显著的是源文件中对Unicode的解释，使得在一个能识别Unicode的编辑器中使用如FUT-8编码成为可能'
# s2 = []
# for k in s:
#     if '\u4e00' <= k <= '\u9fff':
#         s2.append(k)
#
#
# dif = []
# for k in s2:
#     if k not in f.read():
#         dif.append(k)
# f.close()
# f = open('./常用汉字字符串.txt', 'a+', encoding='utf-8')
# print(f.read())
# f.write(''.join(dif))
# f.close()

f = open('./常用汉字字符串.txt', 'r', encoding='utf-8')
print(f.read())
print(len(f.read()))
f.close()