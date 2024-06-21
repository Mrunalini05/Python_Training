#find it is even or odd length of the given linkedlist
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
        
    
    def evenodd(self):                                      #tc: O(n/2)
        t=self.head
        slow=self.head
        fast=self.head
        while (fast!=None and fast.nxt!=None):
            slow=slow.nxt
            fast=fast.nxt.nxt
        if(fast==None):
            print("even length")
        else:
            print("odd length")
            
    '''def evenodd(self):                                    #tc: O(n)
        t=self.head
        c=0
        while(t!=None):
            c=c+1
            t=t.nxt
        if(c%2==0):
            print("even length")
        else:
            print("odd length")'''
        
l1=sll()
l1.head=node(10)                                                                                                                                                                        
l1.addback(20)                                                                                                                                            
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.display()
print()
l1.evenodd()