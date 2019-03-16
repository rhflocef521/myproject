def paixu(n):
    n3=range(0,n)
    for i in n3:
        if i %10==0:
            print()
        print(str(i).rjust(3),end=" ")

