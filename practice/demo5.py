import  random
if __name__ == '__main__':
    # 第一题
    num1 = int(input("请输入第一次要随机生成的整数个数:"))
    mlist = []
    for i in range(0,num1):
        mlist.append(random.randint(0,100))
    print(mlist)

    num2 = int(input("请输入第二次要随机生成的整数个数:"))
    nlist = []
    for i in range(0, num2):
        nlist.append(random.randint(0, 100))
    print(nlist)
    mset=set(mlist)
    nset=set(nlist)
    lset=mset|nset
    print(lset)

    # 第二题
    mstr = input("请输入你的email号：")
    # print(type(mstr))
    mlist=mstr.split("@")
    # print(mlist)
    if len(mlist[0])<6:
            print("姓名长度不能少于6位")
    if mstr.find("@")==-1:
        print("邮箱中必须包含@符号")

    # 第三题
    mstr=str(input("请输入一段字符串："))
    mlist=[]
    for m in mstr:
        mlist.append(m)
    print(mlist)
    nlist=mlist.copy()
    nlist.reverse()
    print(nlist)
    if nlist==mlist:
        print("输入的是回文数")
    else:
        print("不是回文数")

