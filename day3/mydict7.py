if __name__ == '__main__':

    ndict = {"a": 1, "b": 2, "c": 3}

    # 调用字典方法items() 打印该方法的返回值类型和值
    # <class 'dict_items'>
    # dict_items([('a', 1), ('b', 2), ('c', 3)])
    dd = ndict.items()
    print(type(dd))
    print(dd)

    # 调用字典方法keys() 打印该方法的返回值类型和值
    # <class 'dict_keys'>
    # dict_keys(['a', 'b', 'c'])
    ee = ndict.keys()
    print(type(ee))
    print(ee)

    # 调用字典方法values() 打印该方法的返回值类型和值
    # <class 'dict_values'>
    # dict_values([1, 2, 3])
    ff = ndict.values()
    print(type(ff))
    print(ff)

    # 删除字典
    # 删除字典后，字典对象就不能再使用，否则报错
    # NameError: name 'ndict' is not defined
    del ndict
    # print(ndict)


