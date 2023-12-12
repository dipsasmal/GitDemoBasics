"""
def MyFun(*args):
    for arg in args:
        print(arg)

MyFun("Hello",'Welcome',"to","Geeks For Geeks")
"""
def MyFun(arg1, *args):
    print("This is the first non-*args",arg1)
    for arg in args:
        print("This o/p is coming through *args",arg)

MyFun("000",'111','222','333')