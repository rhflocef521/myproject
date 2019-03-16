if __name__ == '__main__':
    # 创建一个非空元祖
    mtuple=(1,2,3,4,5)

    # 此时两个元祖指向同一个地址
    # 相当于传址  ：2078500873936
    #              2078500873936

    ntuple=mtuple
    print(id(mtuple))
    print(id(ntuple))

    # 此时ntuple指向一个新的地址
    ntuple+=mtuple
    print(id(ntuple))


