if __name__ == '__main__':
    # 输入两个字符串
    mstr=" wo shi renhaifeng "
    nstr=" jin nian 24 sui "
    # 对第二个字符串进行左空格去除
    nstr1=nstr.lstrip()
    # 拼接两个字符串
    lstr=mstr+nstr1
    # 打印
    print(lstr)