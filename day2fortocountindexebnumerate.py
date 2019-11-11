nama = 'Hari ini Hari tidak masuk sekolah'
cari = 'h'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlcari = len(nama) - len(x)
print(jmlcari)
print(f'jumlah huruf \'{cari}\' ada = {jmlcari}') ## f untuk apa, untuk ga pakai koma ya?
# harusnya jawabanny 2, nyari hari
cari = 'hari'
x = nama.upper().replace(cari.upper(), '')
print(x)
jmlcari = int(((len(nama)-len(x))/len(cari)))
print(f'jumlahkata \'{cari}\' ada = {jmlcari}')


a = [1,2,1,3,4,5]

for x, y in enumerate(a):
    print(x, y)          # will be separated antara penomoran dengan angka2 dalam list

for x in enumerate(a):
    print (x)          # will be shown in tuple, jadi satu



aenum = dict(enumerate(a))
print(aenum) # dictionary can be enumerated.


