import random
if __name__ == '__main__':
    # 在0-100的范围内 循环10次产生10个随机数
    mlist=[random.randint(0,100) for i in range(0,10)]
    print(mlist)