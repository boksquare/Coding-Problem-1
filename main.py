#Zheng Bok Chia
#1673728

print('Please enter all inputs in numerical formats only')
current_day = int(input('Enter current day:'))
current_month = int(input('Enter current month:'))
current_year = int(input('Enter current year:'))
print('\n')

birth_month = int(input('Enter birth month:'))
birth_day = int(input('Enter birth day:'))
birth_year = int(input('Enter birth year:'))

print('Birthday Calculator\n')
print('Current day:', current_day)
print('Current month:', current_month)
print('Current year:', current_year, '\n')

print('Birthday month:', birth_month)
print('Birth day:', birth_day)
print('Birth year:', birth_year, '\n')

age = 0
if (current_day >= birth_day) & (current_month >= birth_month):
    age = (current_year - birth_year)
else:
    age = (current_year - birth_year - 1)

print('You are', age, 'years old.')

if (current_day == birth_day) & (current_month == birth_month):
    print('Happy Birthday!')
else:
    pass
