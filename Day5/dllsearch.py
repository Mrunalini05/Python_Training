#linear search in double linkedlist
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
        print()
    def addback(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            self.tail.nxt=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if(self.head==None):
            self.head=node(x)
            self.tail=self.head
        else:
            t=node(x)
            t.nxt=self.head
            self.head.prev=t
            self.head=t
            
    def search(self,x):                                       #O(n/2)
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data==x or t1.data==x):
                return "found"
            t=t.nxt
            t1=t1.prev
        if t.data==x:
            return "found"
        else:
            return "not found"
            
            
l1=dll()
l1.addfront(110)
l1.addfront(120)
l1.addback(130)
l1.addfront(10)
l1.addback(20)
l1.addfront(300)
l1.display()
print(l1.search(300))