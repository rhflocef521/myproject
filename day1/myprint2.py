if __name__ == '__main__':
    name="caoerfang"
    sex="women"
    age=18

    #默认print的使用方式 ： caoerfang women 18
    print(name,sex,age)

    #输出不换行，用end参数来实现 ：caoerfang women 18
    print(name,sex,age,end="")

    #参数之间去掉分隔符（一个空格），用sep参数来实现 :caoerfangwomen18
    print(name,sex,age,sep="")