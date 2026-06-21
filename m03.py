class _A :
    def __init__(self):
        print ("A RUN")

class B :
    def __init__(self):
        print ("B RUN")


#雙底線是特殊物件，不可以自己隨便亂創建
#下方的作用是判斷是否為自己呼叫不是別人呼叫的，以免被import執行到
if __name__ == "__main__":
    print (__name__)
    _A()
    B()
else:
    print (__name__)