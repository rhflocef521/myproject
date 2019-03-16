if __name__ == '__main__':
    mlist=[1,2,3,4]
    nlist=[100,503,401,800]
    # m+n :
    # [101, 504, 402, 801, 102, 505, 403, 802, 103, 506, 404, 803, 104, 507, 405, 804]
    qlist=[m+n for m in mlist for n in nlist]
    print(qlist)
    
    # [101, 801, 102, 802, 103, 803, 104, 804]
    plist=[m+n for m in mlist for n in nlist if n%2==0]
    print(plist)