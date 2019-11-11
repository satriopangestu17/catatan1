# def gambar1(q):
#     for w in range(1,q+1,1):
#         for e in range(1,w+1,1):
#             print(e,end='')
#         print()
# gambar1(5)

# def gambar2(w):
#     for i in range(1, w+1,1):
#         for o in range(i,i+1,1):
#             print(str(o)*(o), end='')
#         print()
# gambar2(5)

# def gambar3(r):
#     gambarn= ''
#     for i in range(r,0,-1):
#         for j in range(i,i+1,1):
#             gambarn+= (str(j)+ '')*j
#         gambarn+= ('\n')
#         j-= 1
#     return(gambarn)
# print(gambar3(5))

def gambar3(r):
    gambarn= ''
    for i in range(r,0,-1):
        gambarn+= ('\n')
        for j in range(i,i+1,1):
            gambarn+= (str(j)+ '')*j
            j-= 1
    return(gambarn)
print(gambar3(5))