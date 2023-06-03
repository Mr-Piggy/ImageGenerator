import math

def is_prime(num: int) -> bool:
    if not isinstance(num, int):
        raise TypeError("num must be integer!")
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, math.ceil(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def generate(maxnum: int):
    primelist = ['primes']
    for x in range(maxnum):
        if is_prime(x):
            primelist.append(x)
            #    print(x)
    #    print(primelist)
    return primelist