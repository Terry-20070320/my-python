a = 1 #宣告變數(int)
b = 1.1 #宣告變數(float)
c = "ABC" #宣告變數(字串)

#如果再定義一個相同名稱的變數就會重新宣告覆蓋
a = 2
print (a)

#一次宣告多個變數
a=b=c="這個時候abc都是同樣的變數"
print (a)
print (b)
print (c)

#刪除變數
del a,b,c
#print (a)
#print (b)
#print (c)

#字串處理
a = "abc123" #創建一個字串
print (a) #印出全部
print (a[0]) #指印出第0個 [印出的位置]
print (a[1:3]) #印出第0個到第1個 [指定位置:結束位置]
print (a[1:]) #印出第2個到最後 [指定開始位置:]
print (a*10) #字串*10次印出
print (a+"456") #+號可以在後面加上字串