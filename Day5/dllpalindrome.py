#find the list is palindrome or not in double linkedlist
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
            
    def palindrome(self):
        t=self.head
        t1=self.tail
        while(t!=t1 and t!=t1.nxt):
            if(t.data!=t1.data):
                return "not palindrome"
            t=t.nxt
            t1=t1.prev
        return "palindrome"
            
        
            
            
l1=dll()
#l1.head=node(110)
#l1.tail=l1.head
l1.addfront(1)
l1.addfront(2)
l1.addfront(3)
l1.addfront(3)
l1.addfront(2)
l1.addfront(1)
l1.display()
print(l1.palindrome())