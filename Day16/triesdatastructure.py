#TRIES
#ip: 7
'''   1 school    #1 means insert
      1 world
      1 word
      1 scholar
      2 word        #2 means search
      2 wood
      3 sch          #search the prefix of the given input
'''
#op: True
#      False
#      True

#it is data structure using Tries
#which is reducing the space complexity
'''
w
o o d
r  l  d
d
   s
'''
'''
class node:
    def __init__(self):
        self.d={}
        self.flag=0
        
class tries:
    def __init__(self):
        self.root=node()
        
        
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
        
        
    def search_word(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
            
            
    def search_prefix(self,str):
         t=self.root
         for i in str:
             if i not in t.d:
                 return False
             t=t.d[i]
         return True
       
'''        
'''t1=tries()
t1.insert("world")
t1.insert("word")
t1.insert("wood")
print(t1.search_word("word"))
print(t1.search_word("words"))
print(t1.search_prefix("wor"))
print(t1.search_prefix("wrd"))''''''
t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search_word(s))
    if(a=='3'):
        print(t1.search_prefix(s))
'''    
#op:
'''6
1 word
1 words
2 word
True
3 wo
True
3 wa
False
2 wordss
False'''









#print all the words by the given prefix
#ip: 6
'''  1 word
     1 world
     1 wood
     3 wor
     1 words
'''
#op: word
#      world
#      words
'''
class node:
    def __init__(self):
        self.d={}
        self.flag=0
        
class tries:
    def __init__(self):
        self.root=node()
        
        
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
        
        
    def search_word(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
            
            
    def search_prefix(self,str):
         t=self.root
         for i in str:
             if i not in t.d:
                 return False
             t=t.d[i]
         return True
        
        
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
        

t1=tries()
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search_word(s))
    if(a=='3'):
        print(t1.search_prefix(s))
    if(a=='4'):
        t1.print_all_prefix(s)
'''








#print the prefix from the given list who has longest string in the trie
#ip:
'''     word
        world
        wood
        words
        apple
        apricot
        [b,ba,wo,ap] --->prefixes
'''
#b,ba there is no word with the given prefix
#wo has word,world,wood,words in these longest word is: words and world-->take any one
#ap has apple,apricot in these longest word is: apricot
#compare both words and apricot the longest word with prefix is apricot print: ap

class node:
    def __init__(self):
        self.d={}
        self.flag=0
        
class tries:
    def __init__(self):
        self.root=node()
        
        
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
        
        
    def search_word(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if(t.flag==1):
            return True
        else:
            return False
            
            
    def search_prefix(self,str):
         t=self.root
         for i in str:
             if i not in t.d:
                 return False
             t=t.d[i]
         return True
        
        
    def print_all_prefix(self,str):
        def fun(t,s):
            if(t.flag==1):
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=""
        for i in str:
            if i in t.d:
                s=s+i
                t=t.d[i]
            else:
                return
        fun(t,s)
        
        
    def longest_word(self,prefixes):
        def find_longestword(prefix):
            t=self.root
            for i in prefix:
                if i not in t.d:
                    return
                t=t.d[i]
            longest_word=prefix
            stack=[(t,prefix)]
            while stack:
                node, curr_word=stack.pop()
                if node.is_end_of_word:
                    if(len(curr_word)>len(longest_word)):
                       longest_word=curr_word
                for i,next_node in node.t.d():
                    stack.append((next_node,curr_word+i))
            return longest_word
        best_prefix = ""
        longest_word = ""

        for i in prefixes:
            curr_longest = find_longestword(i)
            if len(curr_longest) > len(longest_word):
                longest_word = curr_longest
                best_prefix = i

        return best_prefix
        

t1=tries()
n=int(input())
prefixes=['b','ab','wo','ap']
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search_word(s))
    if(a=='3'):
        print(t1.search_prefix(s))
    if(a=='4'):
        t1.print_all_prefix(s)
    if(a=='5'):
        print(t1.longest_word(prefixes))








#lexicalorder print the longest word with given prefix
              
              
              
              
              
              
              


#count of no.of prefixes in the given words
#ip: 5
'''  1 word
     1 word
     1 wood
     3 wo
     2 word
'''  
#op: 3
#      True

#count of no.of prefixes without duplicates
#ip: 5
'''  1 word
     1 word
     3 wo
     4 word        #delete
     2 word
'''  
#op: 1
#      False
