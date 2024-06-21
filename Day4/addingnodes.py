#adding a node
'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
            t=head
            while(t!=None):
                print(t.data)
                t=t.nxt
l1=sll()
head=node(10)                                                                                                                                                                        
head.nxt=node(20)                                                                                                                                            
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)
t=head
while(t.nxt!=None):
    t=t.nxt
t.nxt=node(50)
l1.display()
'''

#adding a node at front and back using method
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data)
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
        
l1=sll()
l1.head=node(10)                                                                                                                                                                        
l1.addback(20)                                                                                                                                            
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addfront(1)
l1.display()