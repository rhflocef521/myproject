if __name__ == '__main__':
    # 控制端输入两个人的年龄 默认为int类型
    n1=input("请输入第一个人的生日：")
    n2=input("请输入第二个人的生日: ")
    print(type(n1))
    print(type(n2))
    # 直接比较  如果前者大于后者 则其年龄就小于后者
    if n1>n2:
        print("第一个人的年龄小")
    # 如果前者小于后者 则其年龄就大于后者
    else:
        print("第二个人的年龄小")




