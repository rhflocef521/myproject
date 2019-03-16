if __name__ == '__main__':
    mlist=[1,2,3,4]
    print(mlist)
    print("----------------")
     # 在列表末尾追加数字
    mlist.append(33)
    print(mlist)
    print("----------------")

    # 在列表指定位置添加数字
    mlist.insert(1,44)
    print(mlist)

    print("----------------")
    # 将指定位置的元素弹出
    v=mlist.pop(2)
    print(v)
    print(mlist)

    print("----------------")
    # 将指定列表中的元素删除
    mlist.remove(3)
    print(mlist)


