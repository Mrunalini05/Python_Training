#pairs of each node
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
            
    def pairs(self):
            t=self.head
            while t!=None:
                t1=t.nxt
                while t1!=None:
                    print(t.data,t1.data)
                    t1=t1.nxt
                t=t.nxt
l1=sll()
l1.head=node(10)                                                                                                                                                                        
l1.addback(20)                                                                                                                                            
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
print()
l1.pairs()