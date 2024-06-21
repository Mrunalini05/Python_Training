#find the middle node of the given linkedlist
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
            
    def middlenode(self):
        t=self.head
        slow=self.head
        fast=self.head
        while (fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
        print(slow.data)
        
    '''def middlenode(self):
        t=self.head
        c=0
        while(t!=None):
            c=c+1
            t=t.nxt
        c=c//2
        t=self.head
        for i in range(c):
            t=t.nxt
        print(t.data)'''
    
        
l1=sll()
l1.head=node(10)                                                                                                                                                                        
l1.addback(20)                                                                                                                                            
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
print()
l1.middlenode()