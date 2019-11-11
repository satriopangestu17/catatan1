hari = [ 'mon', 
'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

print(hari[0])

# sekarang hari wed, hari apakah 100 hari lagi?
now = 'wed'

day = 100


carihari = (hari.index(now) + day % len(hari)) % len (hari)

print (f'now', hari [carihari])
print ('now', hari [carihari])

print(len(hari))
print(len(now))

print(hari.index(now))
print(day%len(hari))
print(2%7)

# sekarang hari wed, hari apakah 100 hari yang lalu
hari = [ 'mon', 
'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'mon']

sekarang = 'wed'
days = 100

angkaarray = hari.index(sekarang) - days % len (hari)

print (hari[angkaarray])
# di dalam [] apakah harus integer? karena mau hitung arrayindex?
#note: [] for index tidak bisa minus
# len(hari('mon')); tidak bisa or error

print(hari.count('mon'))

nomor = [1,2,3,4,8,5,6,7,8]
nomor.sort()
print (nomor)

