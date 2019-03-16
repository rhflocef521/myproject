if __name__ == '__main__':
    a1=100
    def mfun():
        global a2
        a2=10
        print("a1={0}".format(a1))
    def mfun2():
        print("a2={0}".format(a2))
    mfun()
    mfun2()