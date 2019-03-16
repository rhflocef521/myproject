import  random
if __name__ == '__main__':
    mynum=[3,2,7,4]
    # 打乱顺序
    random.shuffle(mynum)
    # 打印打乱顺序后的列表
    print(mynum)
    # 对打乱顺序后的列表执行临时排序
    nnum=sorted(mynum,reverse=True)
    print(nnum)