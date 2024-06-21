class node:
    a=5
    def asd():                          #static method-which only access with the class
        print("hii")
    def __init__(self):
        self.b=60
        self.nxt=None
    def qwer(self,x):               #non-static which is accessed by the object or class
        print("hello",self.b,x)
x=node()
print(node.a)
print(a)
print(x.b)
x.qwer()