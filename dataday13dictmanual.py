# data = open('data.txt', 'r')  #r = read
# # a = append
# #w = write
# data = open('data.txt', 'w')
# data.write('test 1 2 3')
# data.write('\ncodingpython')


# data = open('datafileblmada.txt', 'w')
# data.write('test 1 2 3')

# data = open('data.mp4', 'w')
# data.write('my video')

# # data = open('data.py', 'w')
# # data.write('print(\'ok\')')

# data = open('data.mp3', 'w')
# data.write('x = 12')

# data = open('data1.py', 'a')
# data.write('\tprint(x)')
# print(data.readable())
# print(data.read())
# print(data.readlines())
# print(data.readline(10))

##fungsi
# data = open('data.txt', 'r')
# x= data.read()
# print(x)

# data= open('datafungsi.py', 'w')
# data.write(x)

# data= open('data2.txt', 'r')
# x= data.read().split(', ')[::-1]
# print(x)
# print(data.read())

# output = open('data2x.txt', 'a')
# for i in x:
#     output.write(i + '\n')


##file.csv, file.excel
data = open('datacsv.csv', 'w')
data.write('nama,usia,kota\n'+'andi,21,jakarta\n'+'budi,22,bandung\n'+'caca,23,jakarta')

data = open('datacsv.csv', 'r')
x = data.read().split('\n')
print(x)

s = x[0]
print(s)
sp = s.split(',')
print(sp)
sp0 = sp[0] #nama
print(sp0)
sp1 = sp[1] #usia
print(sp1)
sp2 =sp[2] #kota
print(sp2)

d = x[1]
print(d)
dp =d.split(',')
print(dp)
dp0 = dp[0]
print(dp0)
dp1 = dp[1]
print(dp1)
dp2 = dp[2]
print(dp2)

f = x[2]
print(f)
fp = f.split(',')
print(fp)
fp0 = fp[0]
fp1 = fp[1]
fp2 = fp[2]

g = x[3]
print(g)
gp = g.split(',')
print(gp)
gp0 = gp[0]
gp1 = gp[1]
gp2 = gp[2]

dictionary = [{sp0: dp0, sp1:dp1, sp2: dp2},
{sp0:fp0, sp1:fp1, sp2:fp2}, {sp0:gp0, sp1:gp1, 
sp2:gp2}]

# print(dictionary.get(sp0))
print(dictionary)

p = 'oke, sipbang'
print(p.split())




