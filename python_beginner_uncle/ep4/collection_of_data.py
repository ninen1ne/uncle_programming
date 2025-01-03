# 3 Jan 2025 - Nine
# list(array) tuple dictionary

# list
friends = ['Tor', 'Kung', 'feaung']
print(friends)
print(friends[1]) # Kung
print(friends.pop()) # feaung
print(friends)
friends.append('Aom')
friends.remove('Kung')
print(friends)
friends.insert(1, 'John')
print(friends)

for i, f in enumerate(friends):
    print(i, f)
print('------------')

# exercise
thaichar = []
print(ord('ก')) # return ascii code of that char
print(ord('ฮ'))
print(f'index of ฤ: {ord("ฤ")} และ  index of ฦ: {ord("ฦ")}')
start = 3585
for i in range(3585, 3631): 
    thaichar.append(chr(start))
    start+=1

thaichar.remove('ฤ')
thaichar.remove('ฦ')
print(f'{thaichar}\nThis list length: {len(thaichar)}')

# tuple
pets = ('cat', 'dog')

# dictionary
days = {
    'Mon': 'จันทร์',
    'Tue': 'อังคาร',
    'Wed': 'พุธ',
    'Thu': 'พฤหัส',
    'Fri': 'ศุกร์',
    'Sat': 'ดสาร์',
    'Sun': 'อาทิตย์',
}
