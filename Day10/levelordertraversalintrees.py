#levelorder traversal in tree

'''          10
            /  \
          5     15
        / \     /  \
      2   7   11 17
    /  \
   1   3      
'''
#op: 10 5 15 2 7 11 17 1 3


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
            
    def levelordertraversal(self, root):                 #in queue
        if root is None:
            return
        r = []
        r.append(root)
        while r!=[]:
            current = r.pop(0)
            print(current.data, end='-')
            if current.left:
                r.append(current.left)
            if current.right:
                r.append(current.right)
    
        
    
t1=tree()
#t1.create(t1.root,10)
t1.root=node(10)
t1.create(t1.root,5)
t1.create(t1.root,7)
t1.create(t1.root,2)
t1.create(t1.root,15)
t1.create(t1.root,1)
t1.create(t1.root,11)
t1.create(t1.root,3)
t1.create(t1.root,17)
t1.inorder(t1.root)
print()
t1.levelordertraversal(t1.root)