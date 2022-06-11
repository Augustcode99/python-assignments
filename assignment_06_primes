#Task : Print the prime numbers which are between 1 to entered limit number (n).

n = int(input("up to what number would you like to see prime numbers: "))
primes = []
for i in range(2, n+1):
    condition = True
    for ii in range(2, i):
        if (i % ii == 0):
            condition = False
    if condition == True:
        primes.append(i)
primes