if __name__ == '__main__':
    mname=input("your name:")
    # 将format参数按照顺序填写到前面字符串的占位符位置
    print("welcome for your come {0}".format(mname))
    print("{0}对{1}说,{1}爱{0}吗？".format("任海峰","曹二方"))
    print("your name is {name} and your age is {age}".format(name="曹二方",age="23"))
