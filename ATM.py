# cook your dish here
wd,ib=map(eval,input().split())
if wd%5==0 and wd+.5<=ib:
    ib=ib-wd-.5
    print("{0:.2f}".format(ib))
else:
    print("{0:.2f}".format(ib))