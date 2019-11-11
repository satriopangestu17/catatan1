kota = ('jakarta','bandung','surabaya','bogor')
# print(kota[0])
i = 1
while i < len(kota):
    print(kota[i])
    i +=1
    

# # for i in
# print(list(range(6)))

# for i in range(len(kota)):
#     print(kota[i])

# for namakota in kota:
#     print(namakota)

# x='purwadhika'
# for i in x:
#     print(i) # untuk setiap element karakter, for strings

# for i in range(5):
#     print(i)

# # for i in range(2,10,2):
# #     print(i)
# # else:
# #     print('ok') # after iterasi looping selesai tambahin ok

# for i in range(2,10):
#     print(i) # 7 nya ikutan
#     if i == 7: 
#         break

# for i in range(2,10):
#     if i == 7:
#         break
#     print(i) # 7nya ga ikutan

# for i in range(2,10):
#     if i == 7:
#         continue
#     print(i) # 7 ga ikutan, dilompat


# for i in range(2,10):
#     print(i)
#     if i == 7:
#         continue
#     print('a') # diselingi a

# #angka genap wow
# for i in range(1,11):
#     if i%2 == 0:
#         print('WOW')
#     else:
#         print(i)

# #FizzBuzz
# #1-15: , apabila kelipatan 3 print fizz, kalau 5 print buzz, kalau bil kelipatan 3&5 print fizzbuzz
# # for i in range(1,16):
# #     if i%5==0 and i%3 ==0:
# #         print('fizz buzz')
# #     elif i%5 == 0:
# #         print('buzz')
# #     elif i%3 ==0:
# #         print('fizz')
# #     else:
# #         print(i)

# # def fizzbuzz (x):
# #     for i in range(1, x+1):
# #         if i%3==0 and i%5==0:
# #             print('fizz buzz')
# #         elif i %3== 0:
# #             print('fizz')
# #         elif i%5 ==0:
# #             print('buzz')
# #         else:
# #             print(i)
# # fizzbuzz(16)

# #cara pnulisan lain:
def fizzbuzz (x):
    for i in range(1, x+1):
        fizzbuzzni= '' #just show 1 value
        if i%3==0 and i%5==0:
            fizzbuzzni = 'fizz buzz'
        elif i %3== 0:
            fizzbuzzni = 'fizz'
        elif i%5 ==0:
            fizzbuzzni = 'buzz'
        else:
            fizzbuzzni = i
    return fizzbuzzni #return hanya untuk function

print(fizzbuzz(15))