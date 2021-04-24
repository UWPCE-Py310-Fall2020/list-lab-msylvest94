#!/usr/bin/env python

# Series 1
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit_list)

fruit_list.append(input('Add fruit to list: '))
print(fruit_list)

print(fruit_list[int(input('Fruit list entry to display: '))-1])

fruit_list = ['Strawberry'] + fruit_list
print(fruit_list)

fruit_list.insert(0, 'Dragonfruit')
print(fruit_list)

for fruit in fruit_list:
    if fruit[0] == 'p' or fruit[0] == 'P':
        print(fruit)

# Series 2
print(fruit_list)

fruit_list.pop(-1)
print(fruit_list)

fruit_list.remove(input('Which fruit should be removed from the list: '))

# I do no understand what the bonus question is asking me to do

# Series 3

fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

for fruit in fruit_list:
    answer = ''
    while (answer != 'yes') and (answer != 'no'):
        answer = input(f'Do you like {fruit}?')   
        if answer == 'no':
            fruit_list.remove(fruit)
        elif answer != 'yes':
            display('Answer must be yes or no')

print(fruit_list)

# Series 4
fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

fruit_list_to_remove = []

for fruit in fruit_list:
    answer = ''
    while (answer != 'yes') and (answer != 'no'):
        answer = input(f'Do you like {fruit}?')   
        if answer == 'no':
            fruit_list_to_remove.append(fruit)
        elif answer != 'yes':
            display('Answer must be yes or no')

for fruit in fruit_list_to_remove:
    fruit_list.remove(fruit) 

print(fruit_list)