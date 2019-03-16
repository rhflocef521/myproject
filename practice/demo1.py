if __name__ == '__main__':

    # 定义列表
    mlist=['Hello','World','IBM','Apple']
    nlist=[]

    # for循环遍历追加
    for i in mlist :
        nlist.append(i.lower())
    print(nlist)

    olist=['Hello',12.5,'World',6,'IBM',13.14,'Apple']
    plist=[l
           for l in olist
                if not isinstance(l,str)
           ]
    for o in olist:
        if isinstance(o, str):
            plist.append(o.lower())
        else:
            plist.append(o)
    print(plist)