num = int(input())

for c in range(num):
    curr = int(input())
    isPrime = True

    i = 2
    while i * i <= curr:
        if curr % i == 0:
            isPrime = False
            break
        i += 1

    if isPrime and curr != 1:
        print('Prime')
    else:
        print('Not prime')

    isPrime = True
