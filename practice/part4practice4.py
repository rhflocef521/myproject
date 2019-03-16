if __name__ == '__main__':
    # 输入一个字符串为社会主义核心价值观的全拼，每个词用空格进行分隔，将这个字符串，转成列表，遍历输出
    mstr=input("请输入社会主义核心价值观的全拼")
    mlist=mstr.split(" ")
    print(mlist)
    for m in mlist:
        print(m,end="")


