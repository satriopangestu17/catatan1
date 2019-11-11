alphabets = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabets.find('abc'))
string_input = 'makan'
key = 2

n = len(string_input)

string_output = ''

for i in range(n):
    character = string_input[i] # jadi maksudnya i di for, satu2 diperlakukan beda dalam suatu range. bikin variable baru
    location = alphabets.find(character)  # bikin var baru 
    new_location = (location + key) % 26
    string_output += alphabets[new_location] #akhir dimasukkan ke variable string_ouput

print(string_output)





# x = [1,2,3,4] #untuk mengerti for

# for i in x:
#     print(x)


# makanan = ['nanas', 'tempe', 'donut']
# for b in makanan:
#     print (x, b)

# z = 'abc'
# t = 'guk'
# for c in range(2):
#     r = z[c] ##it means that *#*# c in z, tapi ada rangenya
#     z+= 'b'
#     t+= 'i'
#     print(r, z) # untuk mengeti looping, jadi berlanjut looping itu bisa dipakai untuk penggantian tiap huruf dalam kalimat
    
    