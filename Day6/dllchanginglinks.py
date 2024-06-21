#swap the links b/w to numbers only in even length list
#ip: 5 7 8 2 1 4
#op: 7 5 2 8 4 1
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
        
    
    def changelinks(self):                                         #changing the links
        t=self.head
        t1=t.nxt
        t3=None
        while(t!=None):
            t.nxt=t1.nxt
            t1.nxt=t
            t1.prev=t3
            t.prev=t1
            if(t==self.head):
                self.head=t1
            else:
                t3.nxt=t1
            t,t1=t1,t
            t3=t1
        t=t1.nxt
        t1=t1.nxt.nxt
                
            

l1=dll()
#l1.head=node(110)
#l1.tail=l1.head
l1.addback(5)
l1.addback(7)
l1.addback(8)
l1.addback(2)
l1.addback(1)
l1.addback(4)
l1.display()
l1.changelinks()
l1.display()