
# import string
# import collections

# def caesar(rotate_string, number_to_rotate_by):
#     upper = collections.deque(string.asccii_uppercase)
#     lower = collections.deque(string.asccii_uppercase)

#     upper.rotate(number_to_rotate_by)
#     upper.rotate(number_to_rotate_by)
    
#     upper = ''.join(list(upper))
#     lower = ''.join(list(lower))

#     print (upper, lower)
# caesar('mama', 2)
    
alphabets = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabets.find('abc'))
string_input = input('enter your message: ')
key = int(input('enter your key: '))

n = len(string_input)

string_output = ''

for i in range(n):
    character = string_input[i] # jadi maksudnya i di for, satu2 diperlakukan beda dalam suatu range
    location = alphabets.find(character)
    new_location = (location + key) % 26
    string_output += alphabets[new_location]

print(string_output)
    
    