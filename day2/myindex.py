if __name__ == '__main__':

    mstr="good good study , day day up"
    # 在源字符串汇中查找子字符串
    # 返回找到的子字符串的起始下标
    mindex=mstr.index("good")
    print(mindex)

    # 指定下标开始执行查找
    mindex1=mstr.index("good",1)
    print(mindex1)

    # 指定下标结束查找
    mindex2=mstr.index("good",1,10)
    print(mindex2)
