class _A:
    def __init__(self):
        print ("RUN _A")

class B:
    def __init__(self):
        print ("RUN B")
    
    def __AAA (self):
        print ("RUN _AAA")

if __name__ == "__main__":
    print (__name__)
    B()._B__AAA() #呼叫 B()__AAA方法
    _A()
else:
    print (__name__)