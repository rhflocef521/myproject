if __name__ == '__main__':

    mstr="woaicaoerfang";

    mset=set(mstr)
    # 分别输出列表和集合的长度
    print(mstr.__len__())
    print(mset.__len__())

    # 如果列表长度大于集合长度，代表重复
    if mstr.__len__()>mset.__len__():
        print("字符串重复")
    else:
        print("字符串没有重复")

    for i in mset:
        count=0
        for j in mstr:
            if i==j:
                count+=1
        if count>=2:
            print(i,end="")


