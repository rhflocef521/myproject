import random

if __name__ == '__main__':
    s1=int(input("请输入一个整数："))
    s2=int(random.choice(range(10)))

    if s1>s2:
        print(s1)
    else:
        print(s2)