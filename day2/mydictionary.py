if __name__ == '__main__':
    mdict={}

    klist=["name","age","sex"]
    vlist=["cef","24","women"]

    # 键值对 一一对应
    for i in klist:
        mdict[i]=vlist[klist.index(i)]
    print(mdict)

