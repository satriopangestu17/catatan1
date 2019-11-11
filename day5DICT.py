#dictionary
andi = {'name': 'andi', 'age': 22, 'is_married': False, 
'cars' : ['alphard', 'xpander','innova'],
'address' : {'street': 'mawar ungu', 'rt': 5, 'rw':121, 
'kecamatan': 'x', 'zipcode': 123456, 
'geo': {'lat': 111.11, 'lng': 65.89}  } }

print ( andi['name'])
print ( andi['age'])

print(andi.get('name'))
print(andi.get('age')) # enaknya .get kalau tidak ada tidak eror

# .get bisa berfungsi seperti if
print(andi.get('job', 'maaf andi masih nganggur')) # 'Kalau ga ada di dictionary berarti maaf andi masi nganggur' fungsi get jadi ada if else nya
# print(andi['job'])
print(type(andi)) # tipe data dictionary
#cara ganti name jadi budi
andi['name']='budi'
print (andi)
#cars
print (andi['cars'][0])
#address
print (andi['address']['geo'])
#untuk nambahin salay:25000
andi['salary'] = 25000000
#untuk nambahin nomor ktp
andi.update({'no_ktp': 12345678123456})
print(andi)
# coba diubah jadi list
print(list(andi)) #jadi tinggal keynya aja
print(andi.keys()) # untuk liat ada keys apa aja
print(list(andi.keys()))  # untuk liat ada keys apa aja dan jadi list
 #= print(list(andi)) 
print(list(andi.values())) # liat valuesnya aja dan dijadiin list

andiitems = (list(andi.items()))
print (andiitems)
print (andiitems[1][1])