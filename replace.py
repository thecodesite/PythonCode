#Replace strings of a list 

my_list = ['hello', 'world']

result = my_list[0].replace('l', '_')

print(result)  # 👉️ "he__o"


#If you need to call the replace() method on each string in a list, use a list comprehension

my_list = ['hello', 'world']

new_list = [element.replace('l', '_') for element in my_list]

print(new_list)  # 👉️ ['he__o', 'wor_d']
