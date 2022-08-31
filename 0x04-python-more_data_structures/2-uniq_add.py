#!/usr/bin/python3
def uniq_add(my_list=[]):
    dic = {}
    som = 0
    for b in my_list:
        if dic.get(b) is None:
            som += b
            dic[b] = 'full'
    return som
