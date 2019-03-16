if __name__ == '__main__':
    # 创建非空字典
    pdict = dict([("aaaa", 1111), ("bbbb", 2222), ("cccc", 3333)])
    print("pdict={pdictkey}".format(pdictkey=pdict))
    # 遍历数据 (方法一) 直接遍历
    for p in pdict:
        print("pdict[{0}]={1}".format(p, pdict[p]))
    # 遍历数据 (方法二) 获取键
    for q in pdict.keys():
        print("pdict[{0}]={1}".format(q, pdict[q]))
    # 遍历数据 (方法三) 获取值
    for l in pdict.values():
        print("pdict[{0}]={1}".format(l,l.__index__()))
    # 遍历数据 (方法四) 获取键值对
    for k,v in pdict.items():
        print("pdict[{0}]={1}".format(k,v))
