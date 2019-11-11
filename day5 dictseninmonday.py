days = {'senin': 'monday', 'selasa': 'tuesday', 'rabu': 'wednesday',
'kamis': 'thursday', 'jumat': 'friday', 'sabtu': 'saturday', 
'minggu': 'sunday'}
#id to eng

# hari = input('ketik nama hari :')
# input('ketik nama hari:')
# input('bahasa inggrisnya senin=...')
# print(f'bhs inggrisnya {hari.upper()} = {days.get[hari.lower()].upper()}')

#yang bener:
# print(f'bhs inggrisnya {hari.upper()} = {days.get(hari.lower(), "ga ada")}')

# eng to ind
# day = input('write the name:')

# index jumlahnya sama
hari = list(days)
day = list(days.values())

x = input('ketik nama hari:') # atau kalo ga di buat ke input such as, x = 'monday' .#input harus strings; kalau mau ga string tambahin int, float etc
if x.lower() in hari:
    enghari = day[hari.index(x.lower())]
    print(f'bhs inggris{x.lower()} adalah {enghari}')
else:
    idday = hari[day.index(x.lower())]
    print(f'bhs indonesia {x.lower()} adalah {idday}')

# .index(), is not implementedfor set/dictionary
