if __name__ == '__main__':
    # 定义列表
    klist = ["good ", "good ", "study",
             " good ", "good", "study ",
             "good ", " good", " study",
             " good ", "good", " study ",
             "good ", "good ", "study",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up",
             " day ", "day", " up"]
    # 定义一个空列表
    qlist=[]
    # 循环遍历klist 并添加到qlist中
    for k in klist:
        qlist.append(k.strip())
    print(qlist)
    # 将qlist放入集合中 进行去重
    qset=set(qlist)
    print(qset)
    # 定义一个字典
    qdict={}
    for q in qset:
        qdict[q]=qlist.count(q)
    print(qdict)
    #将去重后的set集合中的元素作为值存到字典中
    for q in qset:
        qdict[q]=q
    print(qdict)

