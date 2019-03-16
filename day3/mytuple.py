if __name__ == '__main__':
    #创建元祖 元祖一旦创建 其中的元素都不能被修改
    mtuple=(1,2,3)

    ntuple=mtuple*3
    # 输出两者id 判断是否相等 2821407556520 2821405412472
    print(id(mtuple))
    print(id(ntuple))

    # 元祖的索引操作
    print("mytuple[{1}]={0}".format(mtuple[0],0))

    #元祖的遍历操作
    for m in mtuple:
        print("mtuple==>",m)

    #元祖的分片操作
    ltuple=mtuple[0:3:1]
    print("ltuple =",ltuple)
    #对元祖进行分片 并不会改变id值
    print(id(ltuple))

