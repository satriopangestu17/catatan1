x =range(11) # kalau range di serve seperti list, maka pakai map dan filter ***

def kurangdarilima(x):
    if x < 5:
        return False #tidak ikut di list
    else:
        return True #ikutan di list

y = filter(kurangdarilima, x) #filter untuk memunculkan apa yang ada sesuai syarat if. #map untuk mengeksekusi fungsi di return
print(list(y))



# z = filter(lambda a:True if a>=5 else False, x)
# print(list(z))

# x = pow(2,2)
# y=pow(3,3)
# print(x)
# print(y)

# z=list(map(pow, [2,3], [3,3])) ##* pow bisa jadi function
# print(z)

# x = [1,2,3,4,5]
# y= [1,2,6,7,8]
# z = list(filter(lambda a:a in x, y))
# print(z)
# print((x+z))
# x.remove(1)
# x.remove(2)
# print(x)


# print(2 in x) # apakah ada angka 2 di x

#1x2x3x4 = 24
# angka = [1,2,3,4]
# hasil = 1
# for i in angka:
#     hasil *= i
# print(hasil)

#sama seperti diatas
# from functools import reduce  #reduce untuk dikalikan elemen selanjutnya seperti loop
# z =reduce(lambda x, y: x*y, angka)
# print(z)

#map untuk kombinasi,mengurai antara 2 list.
# a = [2,5,4]
# b = [1,3,2]
# def combi(a,b):
#     return a-b
# x = map(combi,a,b)
# print(x)
# print(list(x))

# kata = ['ini', 'ibu', 'budi']
# print(''.join(kata))

# from functools import reduce #reduce semua elemen di list ikut di proses kalau map satu2
# z = reduce(lambda x, y: x+y, kata) #dapat merubah jadi strings juga
# print(z)

#filter() in map()
# angka = [1,2,3,4]
# z = list(map(lambda x: x * 2, filter(lambda x: x>3, angka)))
# print(z)

#map in filter
angka = [1,2,3,4]
z = list(filter(lambda x: x>3, map(lambda x: x*2, angka)))
print(z) # dikali(map) dulu baru dicari(filter)


##SOAL
#olah angka genap saja, kemudian setiap angka genap dikali 2
#semua angka hasilnya dijumlahkan satu sama lain, soalnya nomor = [1 - 100]

nomor = range(1,101,1)
t = list(map(lambda z: z*2, filter(lambda z: z%2 ==0, nomor)))
print(t)
from functools import reduce
t = reduce(lambda  x,y: x+y, t)
print(t)


nomor = range(1,101,1)
from functools import reduce
t = list(reduce(lambda z,x: z+x, map(lambda z: z*2, filter(lambda z: z%2 ==0, nomor))))

# print(t)  ##??

#bilangan-bilangan prima dari 0-100?

#tentukan apakah prima?
# def prima(x):
#     if x > 1:
#         if x == 2:
#             return True
#         else:
#             for i in range(2, x):  #kalo range nya 1,x bakal false semua
#                 if x % i == 0:
#                     return False
#                     break
#                 else:
#                     return True
#     else:
#         return False

# print(prima(81))

# z = list(filter(prima, range(101)))
# print(z)   belum benar karena 81 dan 99 masuk


# def prima(x):
#     a = False
#     if x > 1:
#         if x == 2:
#             a = True
#         else:
#             for i in range(2, x):  # harus x, karena apabila diisi 101 akan membagi x mulai dari angka 2-101 satu persatu. kalau x, i akan mengikuti jumlah x. 
#                 # print(x, i).why x= intinya karena x dibagi range nya sendiri satu persatu tidak sampai angknya itu sendiri, meskipun ada break
#                 if x % i == 0:
#                     # print(x,i)
#                     a = False                  
#                     break
#                 else:
#                     a = True
#     else: 
#         a = False
#     return a
# print(prima(1))

# z= list(filter(prima, range(101)))
# print(z)


# # l = range(4)
# # def coba(m):
# #     r = []
# #     if m > 1:
# #         for a in range(0, m):
# #             r+= str(a)
# #     else: #kalo ga ada else nilai akan kosong
# #         r = False
# #     return r ## should be in stringg to get in to the [] #list or '' #string
# # l = list(map(coba, l))
# # print(l)

# # l = range(20)
# # def coba(m):
# #     r = []
# #     if m > 10:
# #         return True
# #     else:
# #         for a in range(2, m):
# #             r+= int(a)
# #         return r ## should be in stringg to get in to the [] #list or '' #string
# # print(coba(l))


# ##*integer =artinya ada index keberapanya. contohnya [], dan (1,) * for tuple harus ada komanya baru keitung ada index
# # panjang= (20,)
# # lebar= (15,)
# # tinggi= (2,)
# # def itungluas(x,y,z):
# #     return x*y*z
# # lp = list(map(itungluas, panjang,lebar,tinggi))
# # print(lp)

# ## x % 7 sama dengan x % 7 != 0
# nomor = range(101)
# prime = list(filter(lambda x:(x%7 or x==7) and (x%5 or x == 5) and (x%3 or x==3) and (x%2 or x==2) and (x>1), nomor))
# print(prime)


## x % 7 sama dengan x % 7 != 0
# nomor = range(101)
# prime = list(filter(lambda x:(x%7 or x == 7) and
#  (x%5 or x == 5) and (x%3 or x==3) and (x%2 or x==2) and (x>1), nomor))
# print(prime)

# prima = list(filter(lambda y: y%7 != 0 or y ==7, 
# filter(lambda y:y%5 != 0 or y ==5, filter(lambda y:y%3 != 0 or y ==3,
# filter(lambda y:y%2 != 0 or y ==2,filter(lambda y:y>1, nomor))))))
# print(prima)

# nomor = range(101)
# r = list(filter(lambda x: x%7 or x==7,filter(lambda x: x%5!=0 or x==5,filter(lambda x: x%3 or x==3,filter(lambda x: x%2 or x == 2,
# filter(lambda x: x > 1, nomor))))))

# print(r)

# x = range(0,6)
# z = filter(lambda a:True if a>=5 else False, x)

# print(list(z))

# angka = range(0,101)
# def prima(x):
#     a = False
#     if x > 1:
#         if x== 2:
#             a = True
#         else:
#             for i in range(2, x):
#                 if x % i == 0:
#                     a = False
#                     break
#                 else:
#                     a = True
#     else: 
#         a = False
#     return a

# z = list(filter(prima, range(101)))
# print(z)

# print(0/1)

# x = range(101)   
# def prime(x):
#     # a = True  Perlu?
#     if x > 1:
#         if x == 2:
#             a = True
#         else:
#             for i in range(2, x):
#                 if x % i ==0:
#                     a = False
#                     break
#                 else:
#                     a = True
#     else:
#         a = False
#     return a
# z = list(filter(prime, x))
# print(z)

#
# x = lambda a: 'angka genap' if a % 2 == 0 else 'angka ganjil'

# angka = int(input('masukkan angka yang ingin dites: '))
# y = lambda a : 'bilangan prima' if (a ==2) or (angka % a == 0) else 'bukan bilangan prima'
# print(y(angka))


# def pangkat(x,y):
#     hasil= 1
#     for i in range(y):
#         hasil *= i
#     print(hasil)
# pangkat(3,3)

data = [ {'nama': 'andi', 'usia': 21}, {'nama':'budi', 'usia':22}, {'nama':'caca','usia':23},
{'nama':'deni', 'usia':24} ]
# w = len(data)

for i in data:
    print(i)
