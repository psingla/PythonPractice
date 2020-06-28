cnt = 10
isPrime = 0
number = 1
primeCntr = 2

strNumber = input("Input a number till which you want to identify a prime numbers:")
cnt=int(strNumber)
while number <= cnt:
    primeCntr = 2
    while primeCntr < number:
        if number % primeCntr == 0:
            break
        primeCntr += 1
        if primeCntr == number:
            print(" %i is Prime" % number)
    number += 1

