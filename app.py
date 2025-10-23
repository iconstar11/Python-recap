weight = input('Weight: ')
unit_of_Measure = input('L(bs) or K(g): ')

if unit_of_Measure.upper() == 'K':
    L = int(weight) * 2.2
    print(f'You are {L} pounds')
elif unit_of_Measure.upper() == 'L':
    Kg = int(weight) * 0.45
    print(f'You are {Kg} Kgs')
else: print('Enter a valid unit of measure or weight')

'''name = input('Whats your name? ')


if len(name) < 3:
    print('Name must have more than 2 characters')
elif len(name) > 50:
    print('Name cannot have more than 50 characters')
else: print(f'Hi {name}')
'''
'''temp =9

if temp>30:
    print('Its a hot day')
elif temp<10:
    print('Its a cold day')
else: print('Its neither hot or cold')'''

'''good_credit_worth = False

price = 1000000
good_dic = int(price * 90 /100)
bad_cred_dic = int(price * 80 /100)


if good_credit_worth:
    print(f'You need to put down a payment of ${good_dic} as down payment')
else:
    print(f'You need to put down a payment of ${bad_cred_dic} as down payment')

'''
'''is_hot = False
is_cold = False

if is_hot:
    print('Its a hot day')
elif is_cold:
    print('Its a cold day')
else:
    print('Its a lovely day')
print('Enjoy your day')'''


import math

# === Arithmetic Operations ====

'''
x = 10
y = 3
z = 11
z %= 2

print(z)
print(x + y)
print(x - y)
print(x * y)
print(x ** y)
print(x / y)
print(x // y)
print(x % y)
print(x + y)
print(x + y)
'''

#======Math Functions=====

'''z = 2.4

print(abs(z))
print(math.ceil(z))
'''









'''


lang = 'Python'
target = 'beginners '
title = lang + ' course for' + ' [' + target + '] Hi'

heading = f'{lang} course for [{target}]'
print(heading)

print(len(target))
print(target.find('e'))
print(title.title())
'''





# === Hello World ====

'''print('Antony Titan')

print('0----')
print(' IIII')
print('*' * 10)
'''
''' PYTHON VARIABLES '''
'''price = 10
price = 20
rating = 4.5
_isPublished = True
project = 'Python Recap'

print('price', price)
print('rating', rating)
'''

''' Patient Exercise'''
'''name = 'John Smith'
age = 20
_isNewPatient = True'''

'''name = input('What is your name? ')
color = input('What is your favourite colour? ')
print(name + '\'s favourite colour is ' + color)

'''

'''birth_year = input('What is your year of birth? ')

age = 2025 - int(birth_year)

print(age)'''

'''weight_kg = input('What is your weight in kg\'s? ')

weight_pounds = 2.204623 * float(weight_kg)

print('Your weight is', weight_pounds, 'pounds' )'''