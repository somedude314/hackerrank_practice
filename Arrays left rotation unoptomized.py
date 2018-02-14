def array_left_rotation(a, n, k):
    for i in range (0,k):
        temp = a[0]
        for j in range (1, n):
            a[j-1]=a[j]
        a[n-1]=temp
    print(a)
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
#print(*answer, sep=' ')