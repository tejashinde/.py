# def baseN(num,b,numerals):
#     return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
#
# n = 20
# b = 16
#
# baseN(20,16,"0123456789abcdefghijklmnopqrstuvwxyz")
def typeConversionFunction(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
       return typeConversionFunction(n//base,base) + convertString[n%base]
print(typeConversionFunction(20,16))
