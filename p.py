# -*- coding: utf-8 -*-
import re
with open('./test.txt','r',encoding='UTF-8') as f:
    datas = f.readlines()
    with open('new_file.txt','w',encoding='UTF-8') as new_file:
        for line in datas:
            res = re.search('(.*<location filename=.*)line=.*(/>)',line)
            if res:
                new_file.write(res.group(1)+res.group(2)+'\n')
            else:
                new_file.write(line)