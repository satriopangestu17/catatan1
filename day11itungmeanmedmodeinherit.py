from functools import reduce
class statistik:
    def ratarata(self, x):
        total = reduce(lambda a,b: a+b, x)
        return total / len(x)
    def nilaitengah(self, x):
        x.sort()
        if len(x) % 2 != 0:
            itengah = [int(len(x)/2)]
        else:
            itengah = [int(len(x)/2)-1, int(len(x)/2)]
        atengah = list(map(lambda a: x[a], itengah))
        total = reduce(lambda x,y: x+y, atengah)
        return total / len(atengah)
    def modus(self, x):
        hitung = 0
        angka = 0
        for i in x:
            jumlah = x.count(i)
            if hitung > jumlah:
                continue
            elif hitung <= jumlah:
                hitung = jumlah
                angka = i
        return angka



        

stat = statistik()  ##harus bikin variable gini ketika pakai class , self
print(stat.modus([10,1,3,2,5,4,6,8,8,9]))


# inheritance z dalam y, y dalam x
# class manusia:
#     def __init__(self):
#         self.nama = 'andi'

# class pria(manusia):
#     def __init__(self):
#         manusia.__init__(self)
#         self.olahraga = 'basket'

# class wanita(pria):
#     def __init__(self):
#         pria.__init__(self)
#         self.gender = 'perempuan'
#         self.univ = 'UI'

# obja = wanita()
# print(vars(obja))

# class manusia:
#     def __init__(self, nama):
#         self.nama = nama

# class pria(manusia):
#     def __init__(self, nama, olahraga):
#         manusia.__init__(self, nama)
#         self.olahraga = olahraga

# class wanita(pria):
#     def __init__(self, nama, olahraga, gender, univ):
#         pria.__init__(self, nama, olahraga)
#         self.gender = gender
#         self.univ = univ

# obja = wanita('andi', 'basket', 'wanita', 'UI')
# print(vars(obja))
