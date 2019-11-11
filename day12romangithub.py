# INTEGER TO ROMAN, ##if we use class would be easir if we want to import the edit
# class py_solution:
#     def romandict(self, num):
#         val = [1000, 900, 500, 400, 100, 90,
#         50, 40, 10, 9, 5, 4, 1]
#         syb = ['M', 'CM', 'D', 'CD', 'C',
#         'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#         roman_num = ''
#         i = 0
#         while num >0:
#             for _ in range(num // val [i]):   ##* the result will be integer
#                 # print(_)
#                 roman_num += syb[i]
#                 # print(_)
#                 num -= val[i]
#             i += 1
#         return roman_num
# print(py_solution().romandict(22))


# def romandict(num):
#         val = [1000, 900, 500, 400, 100, 90,
#         50, 40, 10, 9, 5, 4, 1]
#         syb = ['M', 'CM', 'D', 'CD', 'C',
#         'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#         roman_num = ''
#         w = 0
#         while num >0:
#             for a in range(num // val [w]):   ##* the result will be integer, round down. range 0 ga akan muncul apa2 tapi while lanjut
#                 print(a)
#                 # print(_)
#                 roman_num += syb[w]
#                 # print(_)
#                 num -= val[w] ###nyambung pagar 3. ini misalkan 54 akan ngurangi 50 jadi 50 sisa 4. lalu 4 nya akan dicari next loop while
#             w += 1  ###nyambung pagar 3
#             # print(i)
#         return roman_num
# print(romandict(11))


#ROMAN TO INTEGER
# class solution:
#         def romandict(self, s:str) -> int:
#                 dic = {'I':1,
#                 'V':5, 'X':10, 'L': 50,
#                 'C': 100, 'D': 500, 'M': 1000}

#                 total = 0
#                 curr = 0
#                 prev = 0

#                 for i in range(len(s)):
#                         curr = dic[s[i]]
#                         if curr > prev:
#                                 total = total +curr - 2 * prev
#                         else:
#                                 total += curr
#                         prev = curr
#                 return total
# print(solution().romandict('X'))  

# class solution(object):
#         def romandict(self,s):
#                 roman = {'I':1, 'V':5, 'X':10,
#                 'L':50, 'C':100, 'D':500, 'M':1000}
#                 result = 0

#                 for i in range(0,len(s)-1):
#                         c=s[i]
#                         # print(c)
#                         cafter=s[i+1]
#                         print(cafter)
#                         if roman[c]<roman[cafter]:
#                                 result=result-roman[c]
#                         else:
#                                 result=result+roman[c]
#                         # print(result)
#                 result+= roman[s[-1]]
#                 return result
# print(solution().romandict('DMMM'))


# r ={'a':1, 'b':2}
# a = 'a'

# print(a[-1])
# print(r[a[-1]])




# for b in range(5 // 10):
#     print(b)

class solution:
        def romantoangka(self, x):
                roman = {'I':1, 'V':5, 'X':10,
                'L':50, 'C':100, 'D':500, 'M':1000}
                result = 0
                for i in range(0, len(x)-1):
                        a = x[i]
                        aafter = x[i+1]
                        if roman[a] < roman[aafter]:
                                result -= roman[a]
                        else:
                                result += roman[a]
                result+=roman[x[-1]] #posisi disini agar ga kena loop for, yang i in range(0)
                return result
print(solution().romantoangka('IV'))

def angkatoroman(y):
        angka=[1000, 900, 500, 400, 100, 90, 
        50, 40, 10, 9, 5, 4, 1]
        romawi=['M', 'CM', 'D', 'CD', 'C', 'XC',
        'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        z = 0
        hasil = ''
        while y > 0:
                for i in range(y // angka[z]):
                        hasil += romawi[z]
                        y -= angka[z]
                z +=1
        return hasil
print(angkatoroman(1150))
