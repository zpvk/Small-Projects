
check_prime = [26, 39, 51, 53, 57, 79, 85,100]

for num in check_prime:
    factors = []
    for i in range(2,num):
        if num%i == 0:
            factors.append(i)
    if factors==[]:
        print("{} is prime number.".format(num))
    else:
        print("{} This are factors of {}.".format(factors,num))
