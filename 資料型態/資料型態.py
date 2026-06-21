#進位轉換

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

#強制轉換

#int() 強制轉換int
#float() 強制轉換float
X = 1.0
XX = int(X)+2
print (XX,type(XX))

Y = 1
YY = float(Y)+2
print (YY,type(YY))

print ("===============================")

#數值運算常用函式

#abs計算絕對值
X = -5.2
Y = 2.3
print(abs(X),abs(Y))

#pow計算X的Y次方
X = 2
Y = 3.1
print(pow(X,Y))

#round(x)四捨五入
X = 3.5
Y = 2.4
print (round(X),round(Y))

print ("===============================")

#布林Boolean

a = True
b = False
print (type(a),type(b))
print (int(a),int(b))
#True 為 1，False 為 0

#print ("===============================")

#字串 一般是使用單引號或雙引號括起來的資料
#例 A = 'David\'s friend'
#字串有單引號可用倒斜線跳脫或外括號改用雙引號
#str()可以將內容轉換為str

print ("===============================")

#字元
#chr() 函式回傳字元的 ASCII 碼值
c1 = 100
c2 = 50
print (chr(c1),chr(c2))

#ord() 函式回傳字元的 Unicode 碼值
c1 = 'd'
c2 = '2'
print (ord(c1),ord(c2))

#\n可以換行輸出

#字串前加 r，可以防止逸出字元 (例如換行 \n) 被轉譯
str1 = "1\n2\n3"
str2 = r"1'\n'2'\n'"
print (str1)
print (str2)