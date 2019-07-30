X11,Y11=map(int,input().split())
z11=0
for a in range(X11,Y11+1):
    for o in range(1,100):
        if o*o==a:
            z11=z11+1
print(z11)
