if __name__ == '__main__':

    try:
        print(10/0)

    except ZeroDivisionError as e:
        pass

        print("ZeroDivisionError")
        print(e)

    print("well well well")
