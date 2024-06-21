#search the given node present or not
#find the depth of the node which is given
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
            
    def search(self,root,x):
        if(root==None):
            return "not found"
        if(root.data==x):
            return "found"
        elif(root.data>x):
            return self.search(root.left,x)
        else:
            return self.search(root.right,x)
    
            
    def depth(self,root,x,c):
        if(root==None):
            return -1
        if(root.data==x):
            return c
        elif(root.data>x):
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
    
        
    
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
print(t1.search(t1.root,10))
'''if(t1.search(t1.root,10)==1):
    print("found")
else:
    print("not found")
    '''
print(t1.depth(t1.root,7,0))