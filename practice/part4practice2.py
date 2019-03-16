if __name__ == '__main__':
    num=int(input("请输入你要输入的人数"))
    mlist=[]
    for i in range(1,num+1):
        mname=input("请输入第{0}个人的名字：".format(i))
        mlist.append(mname)
    print("排序前：")
    print(mlist)
    for i in range(num):
        for j in range(num-1):
            if len(mlist[j])>len(mlist[j+1]):
                temp=mlist[j]
                mlist[j]=mlist[j+1]
                mlist[j+1]=temp
    print("排序后：")
    print(mlist)