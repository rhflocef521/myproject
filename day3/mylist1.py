if __name__ == '__main__':
    # 指定顺序生成列表
    mlist=list(range(0,10))
    print("mlist={mlistkey}".format(mlistkey=mlist))
    # 生成列表nlist
    nlist=list()
    for i in range(0,10):
        nlist.append(i**2)
    print("nlist={nlistkey}".format(nlistkey=nlist))
    # 复合列表生成式
    plist=[i**2 for i in range(0,10)]
    print("plist={plistkey}".format(plistkey=plist))
    # 复合列表生成式 + if判断
    qlist=[i for i in range(0,10) if i%2==0]
    print("qlist={qlistkey}".format(qlistkey=qlist))