x = 'katak'
y = list(x[::-1])
y = ''.join(y)  #ngubah dari list jadi string
print(y)

# def palindrome(kata):
#     if kata == y:
#         return True
#     else:
#         return False
# print(palindrome(x))

# atau pakai ini sama:
# def palindrome(kata):
#     if kata == x[::-1]:
#         return True
#     else:
#         return False
# print(palindrome(x))

# ata ini, cara lain
def palindrome2(kata):
    for i in range(round(len(kata)/2)):
        palindromekah = False
        if kata[i] == kata[len(kata)-1-i]:
            palindromekah = True
        else:
            palindromekah = False
            break #biar ga keulang
    return palindromekah
print(palindrome2('katak'))
print(palindrome2('oppok'))

# buat function kalo dijalankan bakal jadi 'iah uka gnatnil'
# kalimat = 'hai aku lintang'

# splitkalimat = (kalimat.split())
# splitkalimat.sort(reverse=False)
# print (splitkalimat)

#morse ? #lintang=>

#Caesar Cipher positif
#caesharcipher dari t jadi u. kalo (..., 2)

nama = 'hai aku lintang'
namasplit = nama.split()
print(namasplit)

def ngebalik(l):
    namadibalikin = ''
    for t in l:
        balik = t[::-1] + ' '
        namadibalikin+= balik  # spasi ditambah 
    return namadibalikin

print(ngebalik(namasplit))


#faktorial=
def faktorial(w):
    for r in range(1, w+1):
        if w <= 1:
            return w
        else:
            return w * faktorial(w-1)
print (faktorial(5)) #harus pakai return kalau mau fungsi dalam fungsi

        
