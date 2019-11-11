# password = '12345'
# input('ketik password')
# input('password salah! ketik password:')
# input('password benar")

password = '12345'
inputuser = ''
while inputuser != password:
    inputuser = input('ketik password')
    if inputuser != password:
        print('password salah')
    else:
        print ('password benar')



#ada limit 5 kali masukin salah password berhenti
# password = '12345'
# inputuser1 = ''
# inputuser2 = ''
# inputuser3 = ''
# while inputuser1 != password: #salah ni
#     inputuser1 = input('ketik password')
#     if inputuser1 != password:
#         x = 'password salah'
#         print(x)
#     elif inputuser2 != 'password salah' :
#         print('password salah, tinggal 2 kali kesempatan')
#     else:
#         print ('password benar')  belum kelar salahh ini

#ada limit 5 kali masukin salah password berhenti
#SOAL
# password = '12345'
# input('ketik password')
# input('password salah! ketik password:')
# input('password benar")
#** well programmed **
# password = '12345'
# inputuser = ''  # bikin variable baru ='' untuk membuktikan while sesuai atau benar jadi berlanjut
# jumlahinput = 0
# batasinput = 5
# lebih = False #True and False meaning real true or false
# while inputuser != password and not lebih: #while with two conditions #ditambahkan and not lebih agar berhenti loop whilenya, tapi bakal proses dulu ke if loop while
#     if jumlahinput < batasinput: # because counting from 0,1,2,3,4. then same as 5 elements
#         inputuser = input(f' input ke - {jumlahinput+1} ketik password : ')
#         jumlahinput = jumlahinput + 1                    # jumlahinput += 1
#     else:
#         lebih = True # this one is for stopinggg, because *True will stop while syntax without showing any output and continue to another if conditions. and  False will make an error continuity
# if lebih:
#     print('kesempatan habis, tunggu 24 jam')
# else:
#     print('password benar!')



# # * Hasilnya akan sama seperti diatas. well programmed.

# password = '12345'
# inputpass = '1'
# jumlahinput = 1
# batasinput = 5
# lebih = False

# while password != inputpass and not lebih:
#     if jumlahinput <= batasinput:
#         inputpass = input(f'input pass ke -{jumlahinput }: ')
#         jumlahinput += 1
#     else:
#         lebih = True
# if lebih: #lebih disini artinya True, lanjutan else?
#     print ('coba lagi dalam waktu 24 jam')
# else:
#     print ('password anda benar')


# #*soal sama diatas *if else nya bisa dibalik=
# password = '12345'
# inputpass = '1'
# jumlahinput = 1
# batasinput = 5
# lebih = False

# while password != inputpass and not lebih:
#     if jumlahinput <= batasinput:
#         inputpass = input(f'input pass ke -{jumlahinput }: ')
#         jumlahinput += 1
#     else:
#         lebih = True
# if not lebih: #lebih disini artinya True, lanjutan else?, lanjutan if and not
#     print ('password anda benar')
# else:
#     print ('coba lagi dalam waktu 24 jam')

#* sama hasilnya sama diatas, tapi dibalik true falsenya
# password = '12345'
# inputpass = '1'
# jumlahinput = 1
# batasinput = 5
# lebih = True

# while password != inputpass and lebih:
#     if jumlahinput <= batasinput:
#         inputpass = input(f'input pass ke -{jumlahinput }: ')
#         jumlahinput += 1
#     else:
#         lebih = False
# if lebih: #lebih disini artinya True, lanjutan else?
#     print ('password anda benar')
# else:
#     print ('coba lagi dalam 24 jam')


# password = '12345'
# inputpass =''
# inputpass = input('ketik password')   # has to be after while, so it won't repeat all over again.
# while inputpass != password:
#     if inputpass != password:
#         print('salah')
#     else:
#         print('benar')     # the first on top is the right way.

# password ='12345'
# inputpass='12345'
# while password == inputpass:   # kalau while ==, maka akan mengeluarkan print 'benar' saja, dan tidak akan merepetisi loop
#     inputpass = input('ketik password: ')
#     if inputpass == inputpass:
#         print('benar')
#     else:
#         print('salah') #the first on top is the right way









