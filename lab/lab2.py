def isprime(number): 
    for p in range(2,number):
        x = number % p 
        if x == 0: 
            return False,p
