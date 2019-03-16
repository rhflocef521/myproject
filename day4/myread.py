if __name__ == '__main__':
    mfile=open(r"C:\Users\asus\PycharmProjects\day1\day4\hello.txt","r",encoding="utf-8")
    mbool=mfile.readable()
    print(mbool)

    # 读取全部文件内容
    # val=mfile.read()
    val_readline=mfile.readline()
    # val_readlines=mfile.readlines()
    # print(val_readlines)
    # print(val)
    print(val_readline)

    mfile.close()