if __name__ == '__main__':
    mstr="u can u up , no can no bb"
    # 产看字符串是否以u开头
    mbool=mstr.startswith("u")
    print(mbool)
    print("--------------")

    # 指定范围
    nbool=mstr.startswith("c",4,8)
    print(nbool)