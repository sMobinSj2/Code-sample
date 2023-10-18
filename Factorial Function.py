def factorial(num):
    if type(num) is not int:
        raise TypeError('The number must be an integer')
    if num < 0:
        raise ValueError('The number must be positive')
    if num == 0:
        return 1
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

print(factorial(int(input('Enter your number: '))))