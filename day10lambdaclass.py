

#class = cetakan object
# class mobil:
#     warna= 'merah'
#     tahun= 2010

# #create object mobil
# mobil1 = mobil()
# print(mobil1) #ngasi tau bahwa object
# print(mobil1.warna)
# print(mobil1.tahun)

# mobil2 = mobil()
# print(mobil2.warna)
# print(mobil2.tahun)

# * syntatic sugar .1+.2=...
# class mobilcustom():
#     def __init__(self, warna, tahun, model): #self,reserve word untuk manggil dan bisa customize
#         self.color= warna
#         self.year= tahun
#         self.model= model

# mobil1 = mobilcustom('pink', 2018, ['a','b'])
# mobil2 = mobilcustom('blue',2010, 'q')

# print(mobil1.model)
# print(mobil2.model)

#method
# class mobilcustom():
#     def __init__(self, warna, tahun, model): #self,reserve word untuk manggil
#         self.color= warna
#         self.year= tahun
#         self.model= model
#     def jadul(self):
#         if self.year < 2010:
#             return True
#         else: return False
        
# mobila = mobilcustom('merah', 1998, 'x')
# mobilb = mobilcustom('merah', 2018, 'z')
# print(mobila.year)
# print(mobila.jadul())


# test manggil nama, **iheritance
# class mobil:
#     def __init__(self, warna, seat):
#         self.warna = warna
#         self.seat = seat

# class car(mobil): #**iheritance, car mmewarisi semua method mobil
#     pass

# mobil1 = mobil('pink', 4)
# car1 = car('black', 8)
# print(mobil1.warna, mobil1.seat)
# print(car1.warna, car1.seat)

# class mobil:
#     def __init__(self, warna, seat): 
#         self.warna = warna
#         self.seat = seat

# class car(mobil): #**iheritance, car mmewarisi atau memiliki semua method/komponen mobil
#     gps = True #inheritance gunanya misal ada tambahan gps

# mobil1 = mobil(['black', 'red'], 4)
# car1 = car('black', 8)
# print(mobil1.warna[1], mobil1.seat)
# print(car1.warna, car1.seat, car1.gps)

# class mobil:
#     def __init__(self, warna, seat): 
#         self.warna = warna
#         self.seat = seat

# class car(mobil): #**iheritance, car mmewarisi atau memiliki semua method/komponen mobil
#     def __init__(self, soundsys): # ga bisa jadi bakal punya def fungsi sendiri, sama aja kepisah2
#         self.soundsys = soundsys

# mobil1 = mobil(['black', 'red'], 4)
# car1 = car('buat sound')
# print(mobil1.warna[1], mobil1.seat)
# print(car1.soundsys) ## ga bisa inheritance. kalau mau nambah variable pakai super

# class x:
#     def __init__(self, nama, gelar):
#         self.nama = nama
#         self.gelar = gelar
# class y(x):
#     def __init__(self, nama, gelar):
#         x.__init__(self, nama, gelar)


# ###cara lainnya untuk x = y
# # class y(x):
# #     pass

# # class y(x):
# #     def __init__(self, nama, gelar):
# #         super().__init__(nama, gelar)

# objx = x('andi', 'prof')
# objy = y('budi', 'dr')
# print(objx.nama)
# print(objy.gelar)

#pakai super, inherit dengan y nya memiliki attribute tambahan
# class x:
#     def __init__(self, nama, gelar): #self,reserve word untuk manggil dan bisa customize
#         self.nama = nama
#         self.gelar = gelar

# class y(x):
#     def __init__(self, nama, gelar, univ):
#         super().__init__(nama, gelar)
#         self.kampus = univ

# objx = x('andi', 'M.Sc')
# objy = y('budi', 'Dr', 'UNPAD')
# print(objx.nama)
# print(objy.kampus)

# #untuk memunculkan semua komponen dict
# from pprint import pprint
# pprint(vars(objy))

# print(vars(objy))
# print(getattr(objy, 'gelar'))
# print(hasattr(objy,'warna')) #ga punya warna
# print(hasattr(objy, 'usia')) # ga punya usia

# #cara nambahin attribute di objek
# objy.warna = 'merah'
# # # atau bisa juga menambahkan attribute dengan cara
# setattr(objy, 'alamat', 'BSD')
# print(vars(objy))

# #cara delete
# delattr(objy, 'alamat')
# print(vars(objy))

# class z:
#     nama = 'za'
#     usia = 21
# objz = z()
# print(objz.nama)
# print(objz.usia)

# del z.nama
# print(objz.nama)


#ubah dictionary ke object class
# class student:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia
# class b(student):
#     def __init__(self, nama, usia):
#         super().__init__(nama, usia)
# class c(student):
#     def __init__(self, nama, usia):
#         super().__init__(nama, usia)
# class d(student):
#     def __init__(self, nama, usia):
#         super().__init__(nama, usia)






data = [ {'nama': 'andi', 'usia': 21}, {'nama':'budi', 'usia':22}, {'nama':'caca','usia':23},
{'nama':'deni', 'usia':24} ]

# class student:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia

# for i in data:
#     stud = student(i['nama'], i['usia'])
#     print(f' {stud.nama}, berumur {stud.usia}')


# class x:
#     def __init__(self, nama, gelar):
#         self.nama = nama
#         self.gelar = gelar
# class y(x):
#     def __init__(self, nama, gelar):
#         x.__init__(self, nama, gelar)

nama = 'ultraman'
vars()[nama] = 12345
print(ultraman)


# class student:
#     def __init__(self, nama, usia):
#         self.nama = nama
#         self.usia = usia
#     def createobj(x):
#         nama = x['nama']
#         vars()[nama] = student(x['nama'], x['usia'])
#         return vars() [nama]
#     def createobj(x):
#         return student(x['nama'],x['usia'])  #???


# datanew = list(map(lambda x: student(x['nama'], x['usia']), data))
# print(datanew[0].nama)

# class persegi:
#     def __init__(self, sisi):
#         self.sisi = sisi
#         self.keliling = self.sisi *4
#         self.luas = self.sisi ** 2
# persegia = persegi(4)
# persegib = persegi(8)
# persegic = persegi(10)

# print(vars(persegia)); print(vars(persegib)); print(vars(persegic))

# class keromawi():

# keromawi(1) => I
# keromawi(2019) => MMIX

# #romandict
# roman = {
#     1: I,
#     5: V,
#     10: X,
#     50: L,
#     100: C,
#     500: D,
#     1000: M
# }

# def romadict(x):
#     while x > 1:

# class keangkabiasa




