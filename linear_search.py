a=[1300,1,4,3,5,6,1,600,0,-21,-1]
for x in range (1,len(a)):
    key =a[x]
    #print ("key{}".format(key))
    for y in range (0,x):

        if a[y]>key:
           a[y],key=key,a[y]
           a[x]=key
print a