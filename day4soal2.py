myset = {2,3,1,8,6}
myset = list(myset)
print(myset)
myset.sort(reverse=True)
print(myset)
myset.sort(reverse=False)
print(myset)

# x = {1,2,3}
# y = {5,3,1}
# xuy = x | y
# xuy = list(xuy)
# print (xuy)
# xuy.sort()
# print (xuy)

#bilangan asli, bilangan cacah dari 0

# baru, #frozenset = set yang imutable seperti tuple. dipake ketika index ga penting tapi pingin element nya disitu dan ga dipake
# x = set([1,2,3])
# y = frozenset([1,2,3])
# x.remove(2)
# y.remove(2) # cant  be operated because frozenset
# print(x)
# print(y)