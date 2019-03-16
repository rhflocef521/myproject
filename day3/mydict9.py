if __name__ == '__main__':

    # 定义一个字典
    mlanguage = {"j":"java","c":"c","p":"python"}
    # 按照字典中 key的顺序排序后再输出所有的值
    for l in sorted(mlanguage.keys()):
        print(mlanguage[l])

    # 按照字典中value的顺序排序后再输出所有的值
    for v in sorted(mlanguage.values()):
        print(v)