#Hash Table using Python's Hash Function and open-addressing.

#Linked List created for hash table collision resolution.
class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
        
class LinkedList:
    def __init__(self):
        self.headval=None
    def Print(self):
        i=self.headval
        while(i!=None):
            print(i.dataval)
            i=i.nextval
    def AddToHead(self,val):
        head=Node(val)
        head.nextval=self.headval
        self.headval=head
    def AddToTail(self,val):
        i=self.headval
        if (self.headval==None):
            self.headval=Node(val)
        else:
            while(1):
                if(i.nextval==None):
                    i.nextval=Node(val)  
                    break
                i=i.nextval
    def DelFromHead(self):
        self.headval=self.headval.nextval
    def Delete(self,val):
        i=self.headval
        while(i.nextval!=None):
            if(i.nextval.dataval==val):
                i.nextval=i.nextval.nextval
                return True
            i=i.nextval
        return False
        
#Hash Table Storing Strings. The table rehashes each time the number of values stored is 10 times greater than the number of available slots. 
# The factor for rehashing can be customized.
class HashTable:
    def __init__(self,length):
        self.length=length
        self.values=0
        self.Table=[]
        for j in range(0,length):
            self.Table=self.Table+[LinkedList()]
    def insert(self,string):
        hashed=hash(string)
        hashed=hashed%(self.length)
        (self.Table[hashed]).AddToHead(string)
        self.values=self.values+1
        if((self.values/self.length)>10):
            self.rehash(2*self.length)
    def rehash(self,length):
        ls=[]
        self.length=length
        for i in self.Table:
            j=i.headval
            while (j!=None):
                ls=ls+[j.dataval]
                j=j.nextval
        self.Table=[]
        for j in range (0,length):
            self.Table=self.Table+[LinkedList()]
        for j in ls:
            hashed=hash(j)
            hashed=hashed%(self.length)
            (self.Table[hashed]).AddToHead(j)
    def lookup(self,string):
        hashed=hash(string)%self.length
        j=(self.Table[hashed]).headval
        while (j!=None):
            if (j.dataval==string):
                return True
            j=j.nextval
        return False
    def Delete(self,string):
        hashed=hash(string)%self.length
        ll=self.table[hashed]
        if(ll.headval==string):
            ll.DelFromHead()
        else:
            ll.Delete(string)
