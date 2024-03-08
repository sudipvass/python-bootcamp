#checking prime number or not 
def is_prime(num1):
    if num1 < 1:
        return 'it is not a prime number'
    for num2 in range (2,num1):
        if(num1 % num2 ==0):
            return 'it is not a prime Number'
    return 'it is a prime number'

20-30
20,21,22,23,24