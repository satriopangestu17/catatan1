#edit combined tuple, immutable = tuple(ga bisa diubah), #list=index?

x =  [ (1, ['a','b','c'],3),(4,5,6) ]  #cuma ada satu attribute di list besar awal
x [0][1][2] = 'andi' # [] awal yg luar banget, [] yang dalem pertama, [] yang ddalem index pertama ['a',...]
x [0][1].append('d')
x = tuple(x) #dijadiin tuple
print(x)


# #list
x = [1,2,3]
# y = (1,2,3)
# #set / himpunan, operasi himpunan
# #RULES for set
# #1. no indexing
# #2. duplicate elements not allowed
# #3. set mutable, tp elemen2nya immutable
# z = {1,2,3,1,2,3}
# z.add('a')
# z.add(('c','d','e')) #masuk tambahnya suka2 ga mesti jd plg akhir, karna bukan list
# print(z)
print(tuple(list(set(x)))) # duplicate elements are not computed. hasilnya akan jadi tuple
# print(y[1])
# print(type(z))
# for i in z:
#     print (list(z))
