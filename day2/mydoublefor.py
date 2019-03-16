if __name__ == '__main__':
    mlist=[1,2,3,4,5,6,7,8,9,10]
    nlist=[[1,2,3],[4,5,6],[7,8,9]]
    for clist in nlist:
        for c in clist:
            print("nlist[{1}]={0}".format(c,c.__index__()))

            