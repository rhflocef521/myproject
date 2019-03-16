if __name__ == '__main__':

    ndict={"aa":22,"bb":33,"cc":44}

    # 调用字典方法的get() 打印该方法的返回值类型和值
    # <class 'int'>
    # 结果 : 33
    gndict=ndict.get("bb")
    print(type(gndict))
    print(gndict)

    # 调用字典方法的clear()
    # 打印清空后的字典
    # 结果 ：{}
    ndict.clear()
    print(ndict)

