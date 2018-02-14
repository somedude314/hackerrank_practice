def array_left_rotation(a,n,k):
    b=[0 for x in range (n)]  #must initialize or cannot index! ( eg. myList = [None] * 100)
    for i in range (0,n):
        x = (i+k)%n        #must include brackets!
        b[i]= a[x]

    print(*b, sep=' ')

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
array_left_rotation(a,n,k)