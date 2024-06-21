#swap the length of the list in double linkedlist
#ip: 3 5 7 8 9 10 12 15
#op: 9 10 12 15 3 5 7 8
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
            
    '''def rev_place(self):                                         #swapping data
        fast=self.head
        slow=self.head
        while(fast!=None):
            fast=fast.nxt.nxt
            slow=slow.nxt
        t=self.head
        t1=slow
        while(t1!=None):
            t.data, t1.data=t1.data, t.data
            t=t.nxt
            t1=t1.nxt'''
        
    
    def rev_place(self):                                         #changing the links
        fast=self.head
        slow=self.head
        while(fast!=None):
            fast=fast.nxt.nxt
            slow=slow.nxt
        self.tail.nxt=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.nxt=None
        slow.prev=None
        self.head=slow
        self.tail=t1
            

l1=dll()
#l1.head=node(110)
#l1.tail=l1.head
l1.addback(3)
l1.addback(5)
l1.addback(7)
l1.addback(8)
l1.addback(9)
l1.addback(10)
l1.addback(12)
l1.addback(15)
l1.display()
l1.rev_place()
l1.display()