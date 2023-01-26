for i in range(1, 101):
    print('Fizz'*(i % 3 == 0)+'Buzz'*(1 % 5 == 0) or i)
