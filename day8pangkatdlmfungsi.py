# #iterasi
# # x = [0,1,2,3,4]
# for i in range(5): # untuk setiap i dalam 0,1,2,3,4
#     print(i) 

# x = [[1,2,3],[4,5,6],[7,8,9]]
# for i in x: # [1,2,3], [4,5,6], [7,8,9] ***
#     for j in i:
#         print(j)

# for i in range(5):
#     for j in range(7,9):
#         print(i, 'dan', j)  #posisi print berpengaruh

# i=0 j=7  0 dan 7
# i=0 j=8  0 dan 8
# i=1 j=7  1 dan 7
# dan seterusnya 
# sampai 4 dan 8

#pangkat
# print(2 ** 3)
# print(pow(2,3))

#pangkat dalambentuk fungsi=
def pangkat(x,y):
    out = 1
    for i in range(y):
        out *= x #jadi x=3nya bakal jadi ke loop2 kali 
    print(out)
pangkat(3,2)

# rekursif function: memanggil fungsi dirinya sendiri di dalam fungsi
# def pangkatb(x,y):
#     if(y == 1):
#         return x
#     else:
#         return x * pangkatb(x, y-1) #kalau rekursif harus pakai return
# print(pangkatb(2,3))

# pangkatb(2,3) = 2 * pangkatb(2,2)
# pangkatb(2,2) = 2 * pangkatb(2,1)
# pangkatb(2,1) = 2


# 0! = 1
# 1! = 1
# 2! = 2x1 = 2
#factorial
# def factorial(m):
#     fac = 1
#     for p in range(m):
#         fac *= m
#         m -= 1
#     return fac
# print(factorial(0))

# def faktorial(x):
#     angka = 1 #agar menyamping dan bisa  dikali
#     for i in range(1, x+1):
#         angka *= i
#     return angka
# print(faktorial(4))

# def faktorial2(x):
#     if x <= 2:
#         return x
#     else:
#         return x * faktorial2(x-1) # jika x=5, maka 4*3*2*1=24. which is hasil f(4).
# print(faktorial2(5))




       



