def EvenNumbers(start,end):
    result = []
    for num in range (start,end+1):
        if (num % 2 == 0):
            result.append(num)
    print (result)