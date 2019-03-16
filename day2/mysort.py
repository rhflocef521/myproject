import random
if __name__ == '__main__':

    mynum=[3,5,1,7,2]
    # 由小到大排序
    mynum.sort()
    print(mynum)

    # 打乱顺序 ：①先导入random包 ②调用shuffle()
    random.shuffle(mynum)
    print(mynum)

    # 对打乱后的顺序进行临时排序,降序
    num=sorted(mynum,reverse=True)
    print(num)

    # 对列表进行降序排序
    mynum.sort(reverse=True)
    print(mynum)


