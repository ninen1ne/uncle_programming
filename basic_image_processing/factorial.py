# 22/03/2025 - Nine

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Enter positive integer: '))
print(f'{n}! = {factorial(n)}')
