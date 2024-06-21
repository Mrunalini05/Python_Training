#adding the nodes at front and back and sum of even nodes
#for creating another linkedlist we create the object l2
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):                                                       #constructor for the head
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addfront(self,x):
        if self.head==None:
            self.head=node(x)
        else:
            t=node(x)
            t.nxt=self.head
            self.head=t
    def addeven(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s=s+t.data
            t=t.nxt
        print(s)
    def search(self,x):
        t=self.head
        while(t!=None):
            if(t.data==x):
                return "found"
            t=t.nxt
        return "not found"
        
l1=sll()
l2=sll()
l1.head=node(10)                                                                                                                                                                        
l1.addback(20)                                                                                                                                            
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addfront(1)
l2.head=node(100)
l2.addback(120)
l2.addback(130)
l2.addback(140)
l2.addback(150)
l2.addfront(2)
l1.display()
print()
l2.display()
print()
l1.addeven()
l2.addeven()
print(l1.search(30))