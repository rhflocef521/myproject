if __name__ == '__main__':
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
    qlist=[]
    for k in klist:
        qlist.append(k.strip())
    print(qlist)

    qset=set(qlist)
    print(qset)

    qdict={}
    for q in qset:
        qdict[q]=q
    print(qdict)


    for q in qset:
        qdict[q]=qlist.count(q)
        if qlist.count(q)>=2:
            print(q)
    print(qdict)


