#sum of all nodes
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def display(self):
            s=0
            t=head
            while(t!=None):
                s+=t.data
                t=t.nxt
            print(s)
l1=sll()
head=node(10)                                                                                                                                                                        
head.nxt=node(20)                                                                                                                                            
head.nxt.nxt=node(30)
head.nxt.nxt.nxt=node(40)
l1.display()