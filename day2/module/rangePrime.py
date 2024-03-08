#checking prime number or not 
def is_prime(num1):
    if num1 < 1:
        return False
    for num2 in range (2,num1):
        if(num1%num2 ==0):
            return False
    return True

def prime_Numbers(start,end):
    result=[]
    for num in range(start,end+1):
        if is_prime(num):
            result.append(num)
    print(result)
   
                    