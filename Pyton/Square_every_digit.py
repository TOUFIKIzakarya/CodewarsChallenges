def square_digits(num):
    return int(''.join(map(lambda x : str(int(x)**2), list(str(num)))))