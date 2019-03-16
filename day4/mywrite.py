if __name__ == '__main__':
    mlist=["renhaifeng","caoerfang","woaini"]
    mfile=open(r"C:\Users\asus\PycharmProjects\day1\day4\hello.txt","w")
    # 判断文件是否可读
    mbool = mfile.writable()
    # 向文件写入一段字符
    mwr=mfile.write("meiguanxi")
    print(mwr)

    # 向文件写入多行
    mfile.writelines(mlist)
    mfile.close()