def solve(a0, a1, a2, b0, b1, b2):
    count_a = 0;
    count_b = 0;
    if(a0!=b0):
        if a0 > b0:
            count_a += 1
        else:
            count_b +=1
    if(a1!=b1):
        if a1 > b1:
            count_a +=1
        else:
            count_b+=1
    if(a2!=b2):
        if a2 > b2:
            count_a +=1
        else:
            count_b+=1

    print(count_a, count_b)
    # Complete this function


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
#print(" ".join(map(str, result)))
