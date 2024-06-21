#print bottom view in tree
#ip:
'''         10
            /  \
          5     15
        / \     /  \
      2   7   11 17
    /  \
   1   3
'''
# for 7 and 11, the second element is only taken
#by the vertical level from bottom the ouput is,
#op: 1 2 3 11 15 17


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
            
    def bottomview(self,root):
        if root is None:
            return
        d={}
        q = [(root,0)]
        while q!=[]:
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end='->')
            
    
    
        
d={}    
t1=tree()
#t1.create(t1.root,10)
t1.root=node(10)
t1.create(t1.root,3)
t1.create(t1.root,7)
t1.create(t1.root,2)
t1.create(t1.root,15)
t1.create(t1.root,1)
t1.create(t1.root,11)
t1.create(t1.root,17)
t1.inorder(t1.root)
print()
t1.bottomview(t1.root)