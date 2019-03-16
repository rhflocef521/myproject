def checkSex():
    try:
        name = input("请输入姓名：")
        sex = input("请输入性别：")
        mdict={"man":False,"Mr":False,"boy":False,"male":False,"男":False,
               "women": True, "Mrs": True, "Miss": True,"女":True,"girl":True
               }
        if mdict[sex]:
            print("{0}女士您好".format(name))
        else:
            print("{0}先生你好".format(name))
    except KeyError:
        print("能不能好好输入你的性别？{0}".format(name))


