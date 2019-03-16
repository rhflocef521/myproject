if __name__ == '__main__':
    # 创建非空字典                   key使用了元祖↓
    ldict = {"name": "caoerfang", "sex": "women", ("addr"): "linfen"}
    print(ldict)

    # 创建非空字典 方法一（推荐使用）
    mdict={"a":1,"b":2,"c":3}
    print("mdict={mdictkey}".format(mdictkey=mdict))

    # 创建非空字典 方法二（利用字典的构造器创建 ）
    ndict=dict({"aa":11,"bb":22,"cc":33})
    print("ndict={ndictkey}".format(ndictkey=ndict))

    # 创建非空字典 方法三（利用关键字的方式）
    odict=dict(aaa=111,bbb=222,ccc=333)
    print("odict={odictkey}".format(odictkey=odict))

    # 创建非空字典 方法四（使用包含元祖的列表的方式）
    pdict=dict([("aaaa",1111),("bbbb",2222),("cccc",3333)])
    print("pdict={pdictkey}".format(pdictkey=pdict))



