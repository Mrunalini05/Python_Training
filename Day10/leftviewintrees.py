#print the leftview in tree

'''                       10
                       /       \
                     5         15
                   /   \      /   \
                2      7   11   20
                 \                    \
                   3                   21
                                           \
                                            22
'''
#op: 10 5 2 3 22

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
            
    def leftview(self,root,c):
        if(root==None):
            return
        if c not in r:
            r.append(c)
            print(root.data,c,end="->")
        self.leftview(root.left,c+1)
        self.leftview(root.right,c+1)
    
        

r=[]
t1=tree()
#t1.create(t1.root,10)
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,7)
t1.create(t1.root,2)
t1.create(t1.root,15)
t1.create(t1.root,3)
t1.create(t1.root,11)
t1.create(t1.root,20)
t1.create(t1.root,21)
t1.create(t1.root,22)
t1.inorder(t1.root)
print()
t1.leftview(t1.root,0)