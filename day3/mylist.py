if __name__ == '__main__':
    # 第一种方式
    mlist=list(range(1,10))
    print("mlist={mlistkey}".format(mlistkey=mlist))

    # 第二种方式
    mlist=[]
    for i in range(1,10):
        mlist.append(i*i)
    print("mlist={mlistkey}".format(mlistkey=mlist))

    # 最简单的列表生成式
    mlist=[i*i for i in range(1,10)]
    # '复合'列表生成式
    mlist=[i**2 for i in range(1,10)]
    print("mlist={mlistkey}".format(mlistkey=mlist))

    # ①复杂版的条件判断
    nlist=[]
    for i in range(1,10):
        if i%2==0:
            nlist.append(i)
    print("nlist={nlistkey}".format(nlistkey=nlist))

    # ②'复合'列表生成式+条件判断  (精简版)
    nlist=[i for i in range(1,10) if i%2==0]
    print("nlist={nlistkey}".format(nlistkey=nlist))

    # 第一种方法
    qlist=[1,2,3]
    plist=["a","b","c"]
    olist=[]
    for q in qlist:
        for p in plist:
            olist.append(str(q)+p)
    print("olist={olistkey}".format(olistkey=olist))

    # 第二种方法 笛卡尔积
    qlist = [1, 2, 3]
    plist = ["a", "b", "c"]
    olist=[str(q)+p for q in qlist for p in plist]
    print("olist={olistkey}".format(olistkey=olist))

    # 笛卡尔积+条件判断
    qlist = [1, 2, 3]
    plist = ["a", "b", "c"]
    olist = [str(q) + p
             for q in qlist \
                 if q%2!=0 \
             for p in plist]
    print("olist={olistkey}".format(olistkey=olist))