if __name__ == '__main__':
   #  定义一个字符串
   klist = [ "good ", "good ", "study",
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
        " day ", "day", " up" ]
   # 将列表放入集合中
   kset=set(klist)
   # 分别计算两者的长度大小
   llen=len(klist)
   slen=len(kset)
   # 如果列表长度大于集合长度，则字符串重复
   if llen>slen:
       print("字符串重复")
   else:
       print("字符串无重复")

   # 定义一个列表
   qlist=[]
   # 循环遍历klist并去除空格后追加到qlist中
   for k in klist:
       qlist.append(k.strip())
   print(qlist)
   #  将qlist放入qset中
   qset=set(qlist)
   print(qset)

   # 定义一个字典
   mdict={}
   # 循环遍历qset并输出重复的字符 最后打印字典
   for i in qset:
       mdict[i]=qlist.count(i)
       if qlist.count(i)>=2:
           print(i)
   print(mdict)


