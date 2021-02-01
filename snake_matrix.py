n=int(input())
k=1
for i in range(n):
    print(' '*(n-i-1),end='')
    p=1
    while p and i%2==0:
        for j in range(k, k + n):
            print(j,end=' ')
        p=0
    while p and i%2!=0:
        for j in range(k + n-1, k-1,-1):
            print(j,end=' ')
        p=0
    k += n
    print('')