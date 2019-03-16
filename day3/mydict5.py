if __name__ == '__main__':
    # 创建非空字典
    mdict = dict([("aaaa", 1111), ("bbbb", 2222), ("cccc", 3334)])
    # 利用已经创建的字典创建新的字典，用的是{}
    ndict={k:v for k,v in mdict.items()}
    print(ndict)

    # 在创建字典时指定新字典的过滤条件
    pdict={k:v for k,v in mdict.items() if v%2==0}
    print(pdict)
