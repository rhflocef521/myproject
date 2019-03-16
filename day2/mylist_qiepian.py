if __name__ == '__main__':
    mlist=[1,2,3,4,5,6,7,8,9]
    # 下标如果为负数，列表的最后一个元素的下标为-1。
    # 下标如果为负数，起始下标的值必须小于结束下标的值
    # 下标如果为负数，如果起始下标大于结束下标，则步长必须为负数
    # 切片操作：留头不留尾
    nlist=mlist[0:2]
    for i in nlist:
        print("nlist[{0}]={1}".format(i.__index__(),i))
    print("---------------")
    # 切片操作：三个参数（最后一个表示步长）
    plist=mlist[0:6:2]
    for p in plist:
        print("plist[{0}]={1}".format(p.__index__(),p))
    print("---------------")
    # 切片操作：三个参数（负数下标）
    qlist=mlist[-4:-2]
    for q in qlist:
        print("qlist[{0}]={1}".format(q.__index__(),q))
    print("---------------")
    # 切片操作
    olist=mlist[-3:-6:-1]
    for o in olist:
        print("olist[{0}]={1}".format(o.__index__(),o))
