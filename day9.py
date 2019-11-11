#python: lambda function, annonymous thus can't be recalled
# x = lambda a,b,c : a+b+c
# print(x(2,3,5))
# print(type(x))

# def y(a,b,c):
#     return a+b+c
# print(y(2,3,5))

#lambda bermanfaat untuk fungsi menjadi variable didalam function:
# def myfunction(x):
#     return lambda a : a ** x
# pangkat2 = myfunction(2)
# pangkat3 = myfunction(3)

# print(pangkat2(12))
# print(pangkat3(4))

# x = lambda a : 'genap' if a % 2 == 0 else 'ganjil' # harus satu line
# def y(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# print(x(3))
# print(y(4))

# x = lambda a : print(a)
# x('hello')

## map python: untuk yang iterable. list
# nama = ['andilala', 'budi', 'caca']
# def y(a):
#     return len(a)

# x = map(y, nama) ##* atau bisa x = list(map(y,nama)), maka nanti printnya print(x) saja
# print(list(x))

# map, variable a=string
# def y(a):
#     return len(a)

# x = list(map(y, 'purwadhika'))
# print(x)

#map untuk kombinasi,menggabungkan 2 list.
# a = ['cokelat','melon', 'nangka']
# b = ['apel', 'jeruk', 'nanas']
# def combi(a,b):
#     return a+' '+b
# x = map(combi,a,b)
# print(x)
# print(list(x))

# x = [2,4,6,8,10]
# x = list(map(lambda a: a**2, x))
# print(x)

# x = [2,4,6,8,10]
# b= []
# for i in x:
#     b.append(i ** 2)
# print(b)

# g = [1,2,3]
# g.append(g*2)
# print(g)