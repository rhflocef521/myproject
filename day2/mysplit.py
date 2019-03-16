if __name__ == '__main__':
    mstr=" i am caoerfang"
    # 去除左空格
    nstr=mstr.lstrip()
    # 首字母大写
    print(nstr.capitalize())
    
    # 对字符串切割 ：['good', 'good', 'study,', 'day', 'day', 'up']
    pstr="good good study, day day up"
    qstr=pstr.split(" ")
    print(qstr)
    # 对字符串切割两次： ['good', 'good', 'study, day day up']
    ostr=pstr.split(" ",2)
    print(ostr)
