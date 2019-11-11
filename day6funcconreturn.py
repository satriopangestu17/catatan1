
# students = ['andi', 'budi', 'caca']

# def tes(x):
#     print(x[0])
#     print('caca' in x)

# tes (students) #untuk memunculkan print dari fungsi, ga usa ditambahin print lagi kecuali return

# hvocal =['a','i','u','e','o']
# def vocal(x):
#     if 'a' in x:
#         print (str(x.replace('a', 'o')))
#     if 'i' in x:
#         print (str(x.replace('i','o')))
#     if 'u' in x:
#         print (str(x.replace('u','o')))
#     if 'e' in x:
#         print (str(x.replace('e','o')))
#     else:
#         print (str(x.replace('o','o')))
# vocal('kuda') #wrongg DI FUNGSI, def, GA PERLU ADA IF
    
def vocal(kalimat):
    kalimat  = kalimat.lower()
    kalimat  = kalimat.replace('a','o')
    kalimat  = kalimat.replace('i','o')
    kalimat  = kalimat.replace('u','o')
    kalimat  = kalimat.replace('e','o')
    kalimat  = kalimat.replace('o','o')
    print(kalimat)
vocal('KUda')

def persegipanjang(x, y):
    x += 1
    y += 3
    print(x * y)
persegipanjang(1,2)



# #return func
# def hello():
#     print('hello world!')
# def returnhello():
#     return 'hello return world!'

# hello()
# print(hello())
# returnhello()
# print(returnhello()) #return function seperti value biasa; jadi harus ada print() baru jalan

# def luaspersegi(sisi):
#     print('luas= ', sisi * sisi)
# def luaspersegireturn(sisi):
#     return sisi * sisi

# luaspersegi(4)
# print(luaspersegi(4))
# print(luaspersegireturn(5)) # jadi fungsi return itu bisa punya hasil







