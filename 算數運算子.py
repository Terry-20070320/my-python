#算次方 **
a = 15
b = 10
x = a ** 5  #算次方
print (x)

#只留整數  //
c = a // b
print (c)

#算術運算子優先序
#1. **
#2. * / % //
#3. + -

#比較運算子

#pyuser@deyu ~/zzz$ python
#Python 3.12.9 (main, Aug 14 2025, 00:00:00) [GCC 14.2.1 20250110 (Red Hat 14.2.1-7)] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> a=15
#>>> b=10
#>>> a==b
#False
#>>> a!=b
#True
#>>> a<>b     ## python2 與 != 相同，python3 不適用。
#  File "<stdin>", line 1
#    a<>b
#      ^
#SyntaxError: invalid syntax
#>>> a>b
#True
#>>> a>=b
#True
#>>> a<b
#False
#>>> a<=b
#False
#>>> quit()

#指派運算子  直接把結果派回原變數(不用再多創一個變數做運算)
a = 10 ; a+=5 ; print(a)
a = 10 ; a-=5 ; print(a)
a = 10 ; a/=5 ; print(a)
a = 10 ; a//=5 ; print(a)
a = 10 ; a**=5 ; print(a)

#多重指定變數
a,b,c = 10,11,12
print (a,b,c)

#變數交換
a = 10
b = 20
a,b = b,a
print (a,b)

#邏輯運算
#主要用在組合判斷
#pyuser@deyu ~/zzz$ python
#Type "help", "copyright", "credits" or "license" for more information.
#>>> x=7
#>>> x<10 and x>5
#True
#>>> x<5 or x>10
#False
#>>> not(x<5 or x>10)
#True
#>>> quit()

#身份運算子(主要在判斷是否為同一個物件不是是否一樣)
#pyuser@deyu ~/zzz$ python
#Python 3.12.9 (main, Aug 14 2025, 00:00:00) [GCC 14.2.1 20250110 (Red Hat 14.2.1-7)] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> x=["abc",123]
#>>> y=["abc",123]
#>>> x is y
#False
#>>> x == y
#True
#>>> z=x
#>>> x is z
#True
#>>> quit()

#成員運算子  主要用來判斷序列是否始於該物件
#pyuser@deyu ~/zzz$ python
#Python 3.12.9 (main, Aug 14 2025, 00:00:00) [GCC 14.2.1 20250110 (Red Hat 14.2.1-7)] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> x=["abc",123]
#>>> "abc" in x
#True
#>>> 123 in x
#True
#>>> 12 in x
#False
#>>> 12 not in x
#True
#>>> quit()

#Bitwise 運算子 (記代表符號)
a = 54
b = 41
print (bin(a),bin(b))

#Binary AND
c = a&b
print (c,bin(c))

#Binary OR
c = a|b
print (c,bin(c))

#Binary XOR
c = a^b
print (c,bin(c))

#Binary Ones Complemen
print (bin(a))
print (bin(a),bin(~a))

#Binary Left Shift
print (bin(a))
print (bin(a),bin(a<<2))

#Binary Right Shift
print (bin(a))
print (bin(a),bin(a>>2))