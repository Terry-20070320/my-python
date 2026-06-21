class myc1:
    def __init__(self):
        print ("myc1")

class _myc2:
    def __init__(self):
        print ("_myc2")

if __name__ == "__main__":
    print (__name__)
    myc1()
    _myc2()
else:
    print (__name__)