if __name__ == '__main__':
    mlist=[1,2,3,4,5,6]
    nlist=[44,88,66]
    # 使用extend方法将两个列表合并
    # [44, 88, 66, 1, 2, 3, 4, 5, 6]
    nlist.extend(mlist)
    print(nlist)