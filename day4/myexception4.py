if __name__ == '__main__':
    class MyException(ValueError):
        pass
    try:
        print("手动抛出异常前")
        raise MyException
        print("手动抛出异常后")
    except MyException as me:
        print("抓取我的异常")
    except ValueError as ve:
        print("抓取值异常")
    except Exception as e:
        print("Exception")
        print(e)
    else:
        print("try except else")
    finally:
        print("finally")