if __name__ == '__main__':
    # 定义非空列表
    mstr=[1,2,3,4,5]
    nstr="hehe haha heihei xixi hehe hehe"
    # 计算nstr中hehe的个数
    num=nstr.count("hehe")
    print(num)

    # 指定起始下标并开始执行计数
    num1=nstr.count("hehe",2)
    print(num1)

    # 指定结束下标并结束执行计数
    num2=nstr.count("hehe",2,27)
    print(num2)
    print("")