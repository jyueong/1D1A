a, b = input().split()
print(format(int('0b' + a, 2) + int('0b' + b, 2), 'b'))