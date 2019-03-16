if __name__ == '__main__':

    while True:
        hehe=input("what is your name?")

        if hehe=='q':
             break
        else:
            print(hehe)

    print("我爱你")

    mstr="i love you cao er fang"
    # 倒序输出 ：  gnaf re oac uoy evol i
    print(mstr[::-1])
    # 正序输出 倒数索引为11—1的元素 ：cao er fan
    print(mstr[-11:-1:1])
    s='hello'
    print(s[1])






