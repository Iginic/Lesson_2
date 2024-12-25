numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(0,len(numbers)):
    nn = numbers[i]
    if nn == 1:
        continue
    if nn > 1:
        for j in range(2, i):
            if (nn%j) == 0:
                is_prime = False
                break
        else:
            is_prime = True
    if is_prime:
        primes.append(nn)
    else:
        not_primes.append(nn)
print('Primes:', primes)
print('NOT primes', not_primes)