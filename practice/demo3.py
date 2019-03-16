def jjcfb(n):
    for i in range(0,n+1):
        for j in range(1,i+1):
            print(i, j, sep="*", end="=")
            print(str(i * j).rjust(2, " "), end=" ")
        print()
def sanjiaoxing(n):
    h=n+1
    n1 = range(1, 2 * n)
    for i in n1[0:n]:
        for j in n1[0:n - i]:
            print(" ", end="")
        for j in n1[0:2 * i - 1]:
            print("*", end="")
        print()
    for i in range(1, h):
        for j in range(1, h - i):
            print(end=" ")

        for k in range(1, i + 1):
            print("*", end=" ")
        print()
def lingxing(n):
    n2 = range(1, 2 * n)
    h=n+1
    for i in n2[0:n]:
        for j in n2[0:n - i]:
            print(" ", end="")
        for j in n2[0:2 * i - 1]:
            print("*", end="")
        print()
    for i in n2[0:n - 1]:
        for j in n2[0:i]:
            print(" ", end="")
        for j in n2[2 * (n - i) - 1:0:-1]:
            print("*", end="")
        print()
    for i in range(1, h):
        for j in range(1, h - i):
            print(end=" ")

        for k in range(1, i + 1):
            print("*", end=" ")
        print()
    for b in range(2, h):
        for c in range(2, b + 1):
            print(end=" ")

        for d in range(b, h):
            print("*", end=" ")
        print()