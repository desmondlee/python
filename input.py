# -*- coding: utf-8 -*-

#接收用户输入信息，可通过input()实现：
#input接收的都是str类型，可以根据需要转换，如int()转换成数字：
while(True):
    s = input('birth: ')
    birth = int(s)
    if birth < 2000:
        print('00前')
    else:
        print('00后')