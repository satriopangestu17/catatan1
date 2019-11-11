# d = {'key1':'item1', 'key2':'item2', 
# 'kucing':[3,'jerapah'] }

# print(d['key1'])
# print(d['key2'])
# print(d['kucing'])
# print(d['kucing'][1])

# e = {'key1':{'key2':'item2'}, 
# 'kucing':[3,'jerapah']}

# print(e['key1'])
# print(e['key1']['key2'])
# print(e['kucing'][1])
# print(e.get('key1'))

# t = (1, [0, 'test'], {'a1':True})
# print(t[2]['a1'])
# print(t[1][1])
# t[1][1]='akan'
# print (t[1][1])
# t[1] = 'mark' ## tuple value can't be changed
# print (t[1])

# t = (1, [0,'test'], {'a1':True},(0,{'test':5},2))
# print(t[3][1]['test'])

# #filtering list using set:
# newlist = [1,3, 'test1', 'test2', 2, 3]
# s = set(newlist)
# print(s)
# print(list(s)[2])

#list comprehension, cara mengali 2 semua item di list
# listnum = [1,2,3,4,5]
# listnum= [item*2 for item in listnum]
# print(listnum)


# def times2(num):
#     return num*2
# listnum = [1,2,3,4,5]
# listnum= [times2(item) for item in listnum]
# print(times2(listnum))

#lambda expressions:
# def times2(num):
#     return num * 2
#sama dengan?
# lambda num: num*2

# thus this is for list

#map without lambda(using function):
# listnum = [1,2,3,4,5,]
# def times2(num):
#     return num*2
# listnum = list(map(times2, listnum))
# print(listnum)

# map with lambda(not using function), the result will be the same:
# listnum = [1,2,3,4,5]
# listnum = list(map(lambda num: num*2, listnum))
# print(listnum)

# #filter without lambda (using function):
# def genap(num):
#     return num % 2 == 0
# listnum = [1,2,3,4,5]
# listnum = list(filter(genap, listnum))
# print(listnum)

# # filter using lambda, the reult will be the same:
# listnum = [1,2,3,4,5]
# listnum = list(filter(lambda num: num%2 == 0, listnum))
# print(listnum)

# #methods for searching:
# numlist = [1,2,3]
# input = 'x'
# check1 = input in numlist
# check2 = 'x' in ['x','y','z']
# check3 = 'ka' in 'kurakas'

# print(check1)
# print(check2)
# print(check3)

tulisan1 = ['merdeka', 'hello', 'hellos', 'sohib', 
'kari ayam']

# def cari(x):
#     tulisanbaru = ''
#     for i in tulisan1:
#         if 'ka' in i:
#             return 


#cara mencari ka
tulisan1 = list(filter(lambda t: 'ka' in t, tulisan1))
print(tulisan1)

