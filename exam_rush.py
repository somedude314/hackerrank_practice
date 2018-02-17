def result(times, chap, hrs):
    times.sort()
    sum = 0
    count = 0
    for i in range(0, chap):
        if ((sum + times[i]) > hrs):
            break
        else:
            sum += times[i]
            count += 1
    print(count)


if __name__ == "__main__":
    chap, hrs = input().strip().split(' ')
    chap, hrs = [int(chap), int(hrs)]
    times = []
    init_sum = 0
    for i in range(0, chap):
        #times[i] = int(input().strip())  cannot index list without initializing. can append to it.
        temp = int(input().strip())
        times.append(temp)
        init_sum += times[i]

    if (init_sum <= hrs):
        print(chap)
    else:
        result(times, chap, hrs)
