if __name__ == '__main__':
    print("输入两个数，计算除法")
    print("输入q退出")

    while True:
        print("\t")
        fnum=input("第一个数：")
        if fnum == "q":
            break

        snum=input("第二个数：")
        if snum =="q":
            break

        pinput=input("请输入q")
        if pinput=="q":
            break
    try:
        res=int(fnum)/int(snum)
    except ZeroDivisionError as e:
        print("division error")
    except Exception:
        print("交给我 我能处理")
    else:
        print("result={0}".format(res))
    finally:
        print("处理收尾工作，如果需要的话")