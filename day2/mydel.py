if __name__ == '__main__':
    
    mlist=[1,3,5,6]
    print(id(mlist))
    # 删除下标为0的元素
    del mlist[0]
    print(mlist)
    # 查看mlist的id是否是之前的同一对象
    print(id(mlist))