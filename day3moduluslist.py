
hari = [ 'mon', 
'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

print(hari[::2])
print('mon' in hari)
# ngubah 
hari[1] = 'selasa'
print(hari)
#nambah
hari.append('mon2')
print(hari)
hari.insert(7, 'senin3')
print(hari)
#remove elem
hari.remove('senin3')
print(hari)
hari.pop()
hari.pop()
print(hari)
hari.clear()
print(hari)
#sort dan reverse
hari = [ 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
x = [12, 34, 1 ,10, 19]
x.sort()
print(x)
hari.reverse()
print(hari)
hari = hari[::-1]
print(hari) #ngereverse juga sama
#bikin list dari print
x = 'abcde'
print (list(x))
#copy
x = [1,2,3,4,5,6,7,8,9]
y = x[::2].copy()
print(x)
print(y)
print(y + x)
#list didalam list
z = [ [1,2,3,], [4,5,6], [7,8,9]]
print(z[0][1])
#kalau ada yg sama di list
a = [1,2,3,4,5,6,3]

#cara cari index 
def cariindex(list, i):
    return [x for x, y in enumerate(list) if y == i]
print(cariindex(a,3))


a = [1,2,3]
b = (1,2,3)
print(b[0])
print(type(b)) #tuple is immutable (ga bisa mengubah susunan)
# ngubah tuple jadi list atau sebaliknya
print(list(b))
print(tuple(a))
