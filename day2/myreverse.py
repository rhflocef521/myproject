if __name__ == '__main__':
    # 定义列表
    mynum=[3,5,8,1]
    # 永久反转
    mynum.reverse()
    print(mynum)

    mlist=[1,2,3,4]
    # 打印列表类型
    print(type(mlist))
    # 访问下标为2 
    for l in mlist:
        print("mlist[{0}]={1}".format(l.__index__()-1,l))

    mlist[0]=5
    for i in mlist:
        print(i)

    print("mlist[{0}]={1}".format(mlist[2].__index__()-1,mlist[2]))
