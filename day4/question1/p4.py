def checkNum():
    mstr = str(input("请输入一段字符串："))
    mlist = []
    for m in mstr:
        mlist.append(m)
    print(mlist)
    #
    nlist = mlist.copy()
    nlist.reverse()
    print(nlist)
    if nlist == mlist:
        print("输入的是回文数")
    else:
        print("不是回文数")
