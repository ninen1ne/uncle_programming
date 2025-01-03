import random
from datetime import datetime

# alphabets = 'abcdefg'

# for i in range(10):
#     print(alphabets[random.randint(0, 6)])

# print(f'{(20/3):.2f}')

# print(datetime.now())

thaichar = []
print(ord('ก')) # return ascci of thai char
print(ord('ฮ'))
start = 3585
for i in range(46):
    thaichar.append(chr(start))
    start += 1
print(thaichar)