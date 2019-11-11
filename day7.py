# x = [1,2,3,4,5,6,7]
# y = ['andi', 'budi', 'caca']
# x.reverse()
# print(x)

# #cara 2
# print(x[::-1])

# #3 reversed()
# print(list(reversed(x)))

# for item in range(0, 5, -1):
#     x+= 1
# print (x) xx


# cara ngereverse dengan menggunakan fungsi dan loop
# x = [1,2,3,4,5,6,7]
# y = ['andi', 'budi', 'caca']
# x.insert(0, 7)
# print(x)

# def balikposisi(mylist):
#     hasil = []
#     for i in range(len(mylist)):
#         hasil.insert(0, mylist[i]) #jadi akan berulang2 dari update terbaruny sehingga yang tadinya x[0] menjadi x[1] di varible kosong baru, yaitu hasil
#     return hasil #munculin hasilnya, atau rumus perkalian apa misalnya

# print(balikposisi(x))
# print(balikposisi(y))

x = ['andi', 'budi', 'caca']
# print(x[::-1])
y = [3,5,7,9]
def balikposisi(mylist):
    for e in range(round(len(mylist)/2)): #dibagi 2 untuk tengah2ny
        asli = mylist[e] # e tengahnya sama
        mylist[e] = mylist[len(mylist)-1-e]
        mylist[len(mylist)-1-e] = asli
    return mylist
print(balikposisi(x))
print(balikposisi(y))


##ubah vokal menjadi o =
# def ubahvokal(kata):
#     output = '' #create variable kosong
#     for huruf in kata:
#         if huruf in 'aiueo':
#             output = output + 'o'
#         else:
#             output = output + huruf
#     return output
# print(ubahvokal('kambing')) 


