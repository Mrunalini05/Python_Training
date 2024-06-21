#print the count of prime numbers in the given list
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
            
    def prime(self,t,c):
        if(t==None):
            return c
        def pcount(s,n):
            if(s>=(n//2)+1):
                return 1                                                 #prime
            if(n%s==0):
                return 0                                                 #not prime
            return pcount(s+1,n)
        if(pcount(2,t.data)):
            c=c+1
        return self.prime(t.nxt,c)
            
            
            
            
l1=dll()
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.addback(6)
l1.addback(2)
l1.addback(1)
l1.addback(8)
l1.addback(9)
l1.display()
print(l1.prime(l1.head,0))