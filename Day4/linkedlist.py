#linkedlist

'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
a=node(10)                                                                                                                   #10|obj(b)         ->           20|none
b=node(20)                                                                                                                   #     a                                        b
c=node(30)
a.nxt=b
b.nxt=c
print(a.data,a.nxt)
print(b.data,b.nxt)
print(c.data,c.nxt)
'''

'''class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
head=node(10)                                                                                                         #10|obj(b)         ->           20|obj(c)          ->                  30|None                                                                
head.nxt=node(20)                                                                                                 #      h                                       hn                                             hnn                                               
head.nxt.nxt=node(30)
print(head.data)
print(head.nxt.data)
print(head.nxt.nxt.data)
'''

class node:
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
l1.display()
'''t=head
while(t!=None):
    print(t.data)
    t=t.nxt'''

