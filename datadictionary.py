# import csv

# with open('datacsv.csv', 'r') as x:
#     baca = csv.reader(x)
#     print(list(baca))

# x = ['no', 'nama']
# y = [12, 'andi']
# print(dict(zip(x, y)))


# with open('datacsv.csv', 'r') as x:
#     baca = csv.DictReader(x) #sensitive lower upper case
#     for i in baca:
#         print(dict(i))

import csv
data = [
    {'nama': 'andi', 'usia':22, 'kota':'jakarta'}, 
    {'nama': 'budi', 'usia':22, 'kota':'jakarta'},
    {'nama': 'caca', 'usia':22, 'kota':'jakarta'},
]

with open('datacsv.csv', 'w', newline='') as x:
    kolom = ['nama', 'usia', 'kota']
    a = csv.DictWriter(x, fieldnames=kolom, delimiter='i')
    a.writeheader()
    a.writerows(data)