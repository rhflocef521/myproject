if __name__ == '__main__':
    mstr = "u can u up , no can no bb"
    # 产看字符串是否以b结束
    mbool = mstr.endswith("b")
    print(mbool)
    print("--------------")

    # 指定范围
    nbool=mstr.endswith("b",3,mstr.__len__())
    print(nbool)