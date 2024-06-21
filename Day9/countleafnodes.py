#count and print the leaf nodes
class node:
    def __init__(self,u):
        self.data=u
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
        
    def create(self,root,x):
        '''if self.root is None:
            self.root=node(x)
            return self.root'''
        if(root==None):
            return node(x)
        elif(root.data>x):
            root.left=self.create(root.left,x)
        else:
            root.right=self.create(root.right,x)
        return root
            
            
    def inorder(self,root):
        if(root!=None):
            self.inorder(root.left)
            print(root.data,end='-')
            self.inorder(root.right)
            
            
    def leafnodes(self,root):
        if(root==None):
            return 0
        if root.left==None and root.right==None:
            print(root.data)
            return 1
        return self.leafnodes(root.left)+self.leafnodes(root.right)
    
    
        
    
t1=tree()
#t1.create(t1.root,10)
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,6)
t1.create(t1.root,1)
t1.create(t1.root,20)
t1.create(t1.root,25)
t1.create(t1.root,7)
t1.inorder(t1.root)
print()
print(t1.leafnodes(t1.root))