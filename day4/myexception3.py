if __name__ == '__main__':
    def mfun(v):
        if v==0:
            raise Exception("WELL")
    try:
        mfun(0)
    except Exception as e:
        print("except==>{0}".format(e))
        pass
    print("well well well")