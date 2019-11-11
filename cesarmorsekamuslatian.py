# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# tulisan = input('ketik tulisan: ')
# lompatke = int(input('lompat ke: '))
# n = len(tulisan)
# tulisancesar = ''

# for i in range(n):
#     character = tulisan[i]
#     location = alphabet.find(character)
#     newlocation = (location + lompatke) % 26
#     tulisancesar += alphabet[newlocation]

# print(tulisancesar)

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# tulisan = input('ketik tulisan: ')
# lompatke = int(input('ketik lompatan: '))
# n = len(tulisan)
# tulisancesar = '' 

# for i in range(n):
#     character = tulisan[i]
#     newcharacter = alphabet.find(character)
#     lompatbaru = (newcharacter + lompatke) % 26 # biar balik kebelakang
#     tulisancesar += alphabet[lompatbaru]
# print(tulisancesar)

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# tulisan = input('ketik tulisan: ')
# lompatke = int(input('lompatan: '))
# n = len(tulisan)
# tulisancesar = '' 

# for i in range(n):
#     character = tulisan[i]
#     nocharacter = alphabet.find(character)
#     lompatan = (nocharacter + lompatke) % 26
#     tulisancesar+= alphabet[lompatan]

# print(tulisancesar)

#morse 

# morse = {'a':'._', 'b':'_...', 'c':'_._.', 'd': '_..', 'e':'.',
# 'f':'.._.','g':'__.','h':'....','i':'..','j':'.__','k':'_._','l':'._..',
# 'm':'__','n':'_.','o':'___','p':'.__.','q':'__._','r':'._.','s':'...',
# 't':'_','u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..'}

# kata = 'az'

# def getmorse(x):
#     katamorse = ''
#     for i in kata: #** range isiny angka
#         d= morse[i]
#         katamorse += d + ' '
#     return katamorse
# print(getmorse(kata))


morse = {'a':'._', 'b':'_...', 'c':'_._.', 'd': '_..', 'e':'.',
'f':'.._.','g':'__.','h':'....','i':'..','j':'.__','k':'_._','l':'._..',
'm':'__','n':'_.','o':'___','p':'.__.','q':'__._','r':'._.','s':'...',
't':'_','u':'.._','v':'..._','w':'.__','x':'_.._','y':'_.__','z':'__..',' ':'/'}

# kata = 'satrio pangestu'

# def getmorse(p):
#     tulisanmorse = ''
#     for i in kata:
#         tulis = morse[i]
#         print(tulis)
#         tulisanmorse += tulis + ' '
#     return tulisanmorse
# print(getmorse(kata))

# morsekey= list(morse.keys())
# # print(morsekey)
# morsevalue= list(morse.values())
# # print(morsevalue)
# kata = 'ayam'

# def kamusmorse(p):
#     kamus = ''
#     for i in p.lower():
#         if i in morsekey:
#             kamus += (morse.get(i)) + ' '
#         else:
#             tulis2 = morsekey[morsevalue.index(i)]                                 #bisa ga usa ditulis lagi
#             kamus += tulis2 + ' '
#     return kamus
# print(kamusmorse('e'))


dictio = {'ayam': 'chicken', 'pig':'babi'}
word = 'ayam'

print(dictio.get(word))




        
            
            






