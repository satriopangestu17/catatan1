# sbuah func dengan 1 parameter dimana func tersebut untuk mennetukan value dari parameter tersebut tergolong ganjil atau genap

def gangen(x):
    if float(x%2) == float(0):   ##kalau angka koma masuk ganjil genap?
        print (f'{x} adalah genap')
    else:
        print (f'{x} adalah ganjil')
gangen (1)

# penulisan dengan cara # input:
# def gangen():
#     x = int(input('masukkan angka'))
#     if x%2 == 0:
#         print (f'{x} adalah genap')
#     else:
#         print(f' {x} adalah ganjil')
# gangen()



# sebuah function calculator
# masukkan angka 1:
# masukkan operator aritmatika : + - * / *
# masukkan angka 2: 

# def calc():
#     x = float(input('masukkan angka1 :'))     ##kalau mau pakai input() harus bikin variable baru; bukan ketik calc(x,y,z)
#     op = input('masukkan operator: ')
#     y = float(input('masukkan angka 2: '))
#     if op == '+':
#         print(x+y)
#     elif op == '-':
#         print(x-y)
#     elif op == '*':
#         print(x*y)
#     elif op == '/':
#         print (x/y)
#     else:
#         print('maaf operator tidak dikenali')

# calc ()


# x = 13
# def tes(y):
#     print(x)
# tes(2)  #contoh kesalahan  ati2!








