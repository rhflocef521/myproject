def createUser():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if len(username) > 6 and len(username) < 16:
        print("用户名格式正确")
        if len(password) > 6 and len(password) < 16:
            print("密码格式正确")
            if ("*" and "#" and "!") not in password:
                print("注册成功")
            else:
                print("包含特殊字符*#！")
        else:
            print("密码格式不对")
    else:
        print("用户名格式不对")