if __name__ == '__main__':

    # 创建列表第一种方法
    mstr1=list();
    print(type(mstr1))
    # 创建列表第二种方法
    mstr2=[]
    print(type(mstr2))

    #使用append()在列表尾部添加数据
    mstr2.append("曹二方")
    print(mstr2)

    #使用insert()指定位置来添加数据
    mstr2.insert(0,"任海峰")
    print(mstr2)

    # 使用pop()删除数据；如果不指定参数，则删除列表中最后一个元素
    mstr2.pop(0)
    print(mstr2)

    #使用remove()根据数据来删除数据
    #如果该数据不存在，则抛出异常： ValueError: list.remove(x): x not in list
    mstr2.remove("曹方")
    print(mstr2)

    # 使用del来删除列表
    del mstr2[0]
    # 因为删除了列表，所以此对象不存在 ：name 'mstr2' is not defined
    print(mstr2)