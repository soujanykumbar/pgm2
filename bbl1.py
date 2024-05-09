def bubblesort(a):
    for i in range(len(a)):
        for j in range(i,len(a)-1):
            if a[i] > a[j]:
               a[i],a[j]=a[j],a[i]
a=[10,4,5,16,9,21]
bubblesort(a)
print(a)