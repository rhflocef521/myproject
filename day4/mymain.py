import day4.question1.p1 as pp
import day4.question1.p2 as qq
import day4.question1.p3 as rr
import day4.question1.p4 as ss


if __name__ == '__main__':
    mdict={

            1:"[1]输入用户姓名及性别,让我给你下列的提示",
            2:"[2]随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集",
            3:"[3]注册一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息",
            4:"[4]从键盘输入一行字符串，判断是否是回文数"
    }
    while True:
        for m in mdict.values():
            print(m)

        num = int(input("请选择服务："))
        if num==1:
            pp.checkSex()
        if num==2:
            qq.randnum()
        if num==3:
            rr.checkEmail()
        if num==4:
            ss.checkNum()
        exit(0)






