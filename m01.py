class _a: #只有這個程式可以做使用
    def __init__ (self):
        print ("my first python myPy1")

class b: #所有的程式都可以使用
    def __init__ (self):
        print ("my first python myPy")

_a()
b()