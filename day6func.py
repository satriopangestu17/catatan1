#function
# def hello():
#     print('hello world')  # jadi ga perlu declare fungsinya lagi
# hello();hello()

# def kuadrat(x): #dimasukkan parameter, namanya bebas
#     print(x**2)
# kuadrat(2)
# kuadrat(3)

def pangkat(angka1, angka2):
    print(angka1 ** angka2)
pangkat(2,3)
pangkat(2,10)

pangkat(float(input('ketik angkat1: ')), float(input('ketik angka2: '))) # ditambahin float;karena kalau input doang akan jadi string