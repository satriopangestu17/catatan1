# variables:
# list tuple set dict
#def => prog, return, recursive(fungsi didalam fungsi), lambda (map,reduce,filter)
#loop => while, for, map()
#class, objectfile => csv json

##code template for building objects
# class x:
#     nama = 'x'
#     usia = 12

# objx = x()
# print(x.nama)
# print(objx.nama)
# print(objx.usia)

# #untuk modul or library, kemudian bisa lebih simple daripada bikin dicitonary mulu
# objy = x()
# print(objy.nama)
# print(objy.usia)

# class x:
#     def __init__(self, name, age):  ##self untuk merujuk pada diri ada komponen2nya .nama .usia
#         self.nama = name  
#         self.usia = age
#     def pensiun(self):
#         return 55 - self.usia  ##rumus untuk tau kapan pensiun
# class y(x):
#     pass

# objz = x('budi', 22)
# print(objz.nama)
# print(objz.usia)
# print(objz.pensiun())  ##untuk tau pensiun kapan


# class x:
#     def __init__(self, name, age):  ##self untuk merujuk pada diri ada komponen2nya .nama .usia
#         self.nama = name  
#         self.usia = age
#     def pensiun(self):
#         return 55 - self.usia  ##rumus untuk tau kapan pensiun
# class y(x):
#     def __init__(self, name, age, city):
#         x.__init__(self, name, age)
#         self.kota = city

# objz = x('budi', 22)
# print(objz.nama)
# print(objz.usia)
# print(objz.pensiun())  ##untuk tau pensiun kapan
# objc = x('banu', 19)
# objd = y('ali', 12, 'jakarta')
# print(objd.kota) 
# print(objc.kota)

def fibo(x):
    angka = [1,1]
    for i in range(0,x+1):
        angka.append(angka[i]+angka[i+1])
        
        
    return angka[x]

print(fibo(6))


#cara lain rekursif:
# def fibo(urutan):
#     if urutan < 2:
#         return urutan
#     else:
#         return fibo(urutan-1) + fibo(urutan-2)

##cara lain, rekursif hasil in class:
# class Fibo:
#     def fibo(self, urutan):
#         if urutan < 2:
#             return urutan
#         else:
#             return self.fibo(urutan-1) + self.fibo(urutan-2)
# Fibo = Fibo()
# print(Fibo.fibo(1))




# x = 'AbcdEFghI'
#     return function => 'aBCDefGhI'

q = 'AbcdEFghI'
# print(q.index('A'))
# print(q[0])
# u = (list(q))
# y = 'a'
# ybaru = y.replace(y, y.upper())
# print(ybaru)
# if y == y.lower():

# print(y.split())
# print(y is y.lower())

def abc(y):
    z = ''
    for e in y:
        # print(e)
        if e.isupper():
            ebaru = e.lower()
            z += ebaru
        else:
            ebaru = e.upper()
            z += ebaru   
    return z    
print(abc(q))




