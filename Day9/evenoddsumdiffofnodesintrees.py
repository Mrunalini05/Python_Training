#sum of even nodes and odd nodes in trees
#difference between even sum and odd sum print by the single method. (not call two methods and subtract)
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
            
            
    def evensum(self,root):
        if(root==None):
            return 0
        if(root.data%2==0):
            return root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            return self.evensum(root.left)+self.evensum(root.right)
    
    def oddsum(self,root):
        if(root==None):
            return 0
        if(root.data%2!=0):
            return root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            return self.oddsum(root.left)+self.oddsum(root.right)
        
    '''def diff(self,root):
        es=0
        os=0
        if(root==None):
            return 0
        if(root.data%2==0):
            es+=root.data+self.evensum(root.left)+self.evensum(root.right)
        else:
            es+=self.evensum(root.left)+self.evensum(root.right)
        if(root.data%2!=0):
            os+=root.data+self.oddsum(root.left)+self.oddsum(root.right)
        else:
            os+=self.oddsum(root.left)+self.oddsum(root.right)
        return abs(es-os)'''
    
    def diff(self,root):
        if root==None:
            return 0
        if(root.data%2==0):
            return root.data+self.diff(root.left)+self.diff(root.right)
        return self.diff(root.left)+self.diff(root.right)-root.data
    
    
t1=tree()
#t1.create(t1.root,10)
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,7)
t1.create(t1.root,1)
t1.create(t1.root,20)
t1.create(t1.root,25)
t1.inorder(t1.root)
print()
print(t1.evensum(t1.root))
print(t1.oddsum(t1.root))
#print(abs((t1.evensum(t1.root))-t1.oddsum(t1.root)))
#print(t1.diff(t1.root))
print(abs(t1.diff(t1.root)))
