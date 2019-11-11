z = {1,2,3,1,2,3}

z.update('andi') # to add 'andi' to the set
z.update((6,7,8))
z.update({'z', 'budi'})
# z.remove('budi')
# z.discard('budi')
print(z)
z.pop()
print(z)
print('budi' in z) #apakah ada elemen budi
# z.clear() #to null the set
# del (z)  #untuk menghilangkan set z 
print(z)