class orang:
    nama = 'budi'
class manusia:
    nama = 'budi'
    def __init__(self, nama):
        self.nama = nama
    
obja = manusia('andi')
objb = orang()
print(vars(obja))
print(objb.nama)

# class manusia:
#     def __init__(self, nama):
#         self.nama = nama

# class pria(manusia):
#     def __init__(self, nama):
#         manusia.__init__(self, nama)
#         self.gender = 'laki laki'

# class wanita(manusia):
#     def __init__(self, nama):
#         manusia.__init__(self, nama)
#         self.gender = 'wanita'
#         self.pendidikan = 'S1'

# obja = manusia('andi')
# objb = pria('andi')
# objc = wanita('andi')
# print(vars(obja))
# print(vars(objb))
# print(vars(objc))

# multi 
class x:
    def __init__(self, nama):
        self.x = nama

class y(x):
    def __init__(self, nama, kerja):
        x.__init__(self, nama) #atau bisa pakai cara super
        self.y = kerja
        
class z(y):
    def __init__(self, nama, kerja, alasan):
        y.__init__(self, nama, kerja)
        self.z = alasan

objb = z('andi', 'pns', 'why')
print(vars(objb))


# multiple inheritance
class karnivora:
    def __init__(self):
        self.daging= True
        self.nama = 'yongke'

class herbivora:
    def __init__(self):
        self.tumbuhan= True
        self.age= 35

class omnivora(karnivora, herbivora): #inherit to karnivora and herbivora
    def __init__(self):
        karnivora.__init__(self)
        herbivora.__init__(self)
        self.mcd = True

obja = omnivora()
print(vars(obja))
print(omnivora.__mro__)

