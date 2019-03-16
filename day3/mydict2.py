if __name__ == '__main__':

    # 创建非空字典
    mdict={"name":"caoerfang","sex":"women"}
    # 修改字典 下标改用字符串 也就是key
    mdict["name"]="caogongju"
    # 打印
    print(mdict)

    # 删除键值对 使用del 下标改用字符串 也就是key
    del mdict["sex"]
    print(mdict)

    # 创建非空字典
    pdict = dict([("aaaa", 1111), ("bbbb", 2222), ("cccc", 3333)])
    print("pdict={pdictkey}".format(pdictkey=pdict))
    # 访问数据
    p1 = pdict["aaaa"]
    print("pdict[aaaa]=", p1)
    # 删除数据
    del pdict["cccc"]
    print(pdict)
