if __name__ == '__main__':
    m9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = int(input("请输入一个数："))
    for i in m9[0:num]:
        for j in m9[0:i]:
            print(i, j, sep="*", end="=")
            print(str(i*j).rjust(2," "), end=" ")
        print()