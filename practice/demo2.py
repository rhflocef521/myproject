if __name__ == '__main__':

    # 创建列表Klist
    klist = ["good ", "good ", "study",
             " good ", "good", "study ",
             "good ", " good", " study",
             " good ", "good", " study ",
             "good ", "good ", "study",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up"]
    # 创建字典
    mlist=[]
    for k in klist:
        mlist.append(k.strip())
    print(mlist)

    # 去重
    mset=set(mlist)
    print(mset)

    # 创建字典
    mdict={}
    for m in mset:
        mdict[m]=mlist.count(m)
    print(mdict)

    # 创建字典
    ndict={}
    for i in mset:
        ndict[i]=i
    print(ndict)
