import day4.question2.p1 as pp
import day4.question2.p2 as qq
import day4.question2.p3 as rr
import day4.question2.p4 as ss

if __name__ == '__main__':
    mdict={
        1:"[1]对一字符串进行翻转操作",
        2:"[2]存储公司10个名单,按姓名的字符多少来排",
        3:"[3]输入用户名密码进行注册，要求用户名允许数字字母6-16位，密码6-16位，不允许出现*#!",
        4:"[4]输入一个字符串为社会主义核心价值观的全拼，每个词用空格进行分隔，将这个字符串，转成列表，遍历输出",
    }
    while True:
        for i in mdict.values():
            print(i)

        num=int(input("请输入你要选择的服务："))
        if num==1:
            pp.reNum()
        if num==2:
            qq.soName()
        if num==3:
            rr.createUser()
        if num==4:
            ss.hexin()

