if __name__ == '__main__':
    # 顺序产生10个数 并求平方
    squares=[val**2 for val in range(1,11)]
    print(squares)

    mlist=[1,3,5,7,9,2,4,6,8,10]
    for m in mlist:
         print("mlist[{0}]={1}".format(m.__index__(),m))
    #使用range来初始化一个list
    nlist=[i for i in range(1,10)]
    print(nlist)