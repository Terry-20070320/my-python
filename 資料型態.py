#0b是代表2進制 bin函式是轉成二進制
A = 0b0111
print (A)
print (bin(A))

#0o是代表8進制 oct函式是轉成八進制
B = 0o037
print (B)
print (oct(B))

#0x是代表16進制 hex函式是轉成十六進位
C = 0x3F
print (C)
print(hex(C))

print ("===============================")


#int() 強制轉換int
#float() 強制轉換float
X = 1.0
XX = int(X)+2
print (XX,type(XX))

Y = 1
YY = float(Y)+2
print (YY,type(YY))