if __name__ == '__main__':
    # 创建非空字典
    mdict={"name":"caoerfang","sex":"women",("address"):"linfen"}

    #将字典转换成字符串类型
    ndict=str(mdict)

    #打印类型 打印显示字典
    print(type(ndict))
    print(ndict)

    # 求字典的长度 ---用len()
    lmdict=len(mdict)
    print(lmdict)

    # 求字典的类型 ---用type()
    tmdict=type(mdict)
    print(tmdict)