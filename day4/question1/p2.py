import  random
def randnum():
    num1 = int(input("请输入第一次要随机生成的整数个数:"))
    mlist = []
    for i in range(0, num1):
        mlist.append(random.randint(0, 100))
    print(mlist)

    num2 = int(input("请输入第二次要随机生成的整数个数:"))
    nlist = []
    for i in range(0, num2):
        nlist.append(random.randint(0, 100))
    print(nlist)

    mset = set(mlist)
    nset = set(nlist)
    lset = mset | nset
    print(lset)

