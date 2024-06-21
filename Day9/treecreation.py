#tree creation
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
        
    def create(self,root,x):
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
    
t1=tree()
t1.create(t1.root,10)
t1.create(t1.root,5)
t1.create(t1.root,7)
t1.create(t1.root,1)
t1.create(t1.root,20)
t1.create(t1.root,25)