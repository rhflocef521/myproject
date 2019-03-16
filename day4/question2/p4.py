def hexin():
    mstr = input("请输入社会主义核心价值观的全拼")
    mlist = mstr.split(" ")
    print(mlist)
    for m in mlist:
        print(m, end="")
