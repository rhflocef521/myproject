if __name__ == '__main__':
    mlist=[1,3,7,9,5,6,4,2]
    # 通过已有列表创建新的列表
    nlist=[n for n in mlist]
    # 打印两者id 看是否相同：2335900525064
    #                      2335900525128
    print(id(mlist))
    print(id(nlist))