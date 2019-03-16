if __name__ == '__main__':
    try:
        mfile=open(r"C:\Users\asus\PycharmProjects\day1\day4\hello.txt")
    except OSError:
        print("oserror")
    except Exception:
        print("Exception")
    else:
        mfile.close()


