if __name__ == '__main__':
    h=int(input("请输入行数："))
    n9=range(1,2*h)
    for i in n9[0:h]:
        for j in n9[0:h-i]:
            print(" ",end="")
        for j in n9[0:2*i-1]:
            print("*",end="")
        print()
    for i in n9[0:h-1]:
        for j in n9[0:i]:
            print(" ",end="")
        for j in n9[2*(h-i)-1:0:-1]:
            print("*",end="")
        print()
    for i in range(h+1):
        print(" "*(h-i),end="")
        print(" *"*i,sep=" ")



