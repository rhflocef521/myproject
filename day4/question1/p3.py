def checkEmail():
    # 客户端输入
    mstr = input("请输入你的email号：")
    # print(type(mstr))
    mlist = mstr.split("@")
    # print(mlist)
    if len(mlist[0]) < 6:
        print("姓名长度不能少于6位")
    if mstr.find("@") == -1:
            print("邮箱中必须包含@符号")
       