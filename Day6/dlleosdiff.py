# find even and odd sum and make and print the difference
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
        
    def eodiff(self,t,es,os):                                            #in recursion
        if(t==None):
            return abs(es-os)
        if(t.data%2==0):
            es=es+t.data
        else:
            os=os+t.data
        return self.eodiff(t.nxt,es,os)
    
    '''def eosd(self):
        es=0
        os=0
        t=self.head
        while(t!=None):
            if(t.data%2==0):
                es=es+t.data
            else:
                os=os+t.data
            t=t.nxt
            diff=abs(es-os)
        return es,os,diff
'''
        
#l1.head=node(110)
#l1.tail=l1.head
l1=dll()
l1.addback(3)
l1.addback(4)
l1.addback(5)
l1.addback(6)
l1.addback(2)
l1.addback(1)
l1.addback(8)
l1.addback(7)
l1.display()
#print(l1.eosd())
a=l1.eodiff(l1.head,0,0)
print(a)