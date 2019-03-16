import random
if __name__ == '__main__':

  # 定义一个空列表
  nlist=[]
  # 随机生成并追加元素到序列中
  for i in range(1,10):
      nlist.append(i)
  print(nlist)
  print(type(nlist))
  # 随机生成一整数
  n2=random.randrange(0,20)
  print(n2)
  # 循环遍历列表 看元素是否在序列中
  for i in nlist:
      if n2==i:
          print("{0}在序列中".format(n2))

