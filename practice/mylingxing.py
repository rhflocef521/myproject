if __name__ == '__main__':
    # 讲输入的行数转换为int类型
    n=int(input("请输入行数:"))
    n9=range(1,n*2)
    for i in n9[0:n]:
        for j in n9[0:n-i]:
            print(" ",end="")
        for j in n9[0:2*i-1]:
            print("*",end="")
        print()
    for i in n9[0:n-1]:
        for j in n9[0:i]:
            print(" ",end="")
        for j in n9[2*(n-i)-1:0:-1]:
            print("*",end="")
        print()