if __name__ == '__main__':
    mstr="20"
    # 将准备好的字符串按照长度10进行补齐
    # 剩下的部分用“-”来补全
    nstr=mstr.ljust(10,"-")
    print("nstr==>",nstr)
    print("----------------")

    # 将准备好的字符串按照长度10进行补齐
    # 剩下的部分用“+”来补全
    lstr=mstr.rjust(10,"+")
    print("lstr==>",lstr)