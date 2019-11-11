#dict
student = {'name' : 'rio', 'age' : 25, 'courses' : ['math', 'science']}
print(student['name'])

# #func
def times2(num):
    return num * 2
print(times2(1))

listnum = [1,2,3,4,5]
listnum = [times2(item) for item in listnum]
print(listnum)

# #tuples, thus in [] can't be tuple
t = (1, [0, 'test'], { 'a1' : True})

print(t[2]['a1']) # a1 is not integer but it can be in []
print(t[1][1])

##*** if the file folder's name contains symbol like &,$, etc. would be error.
