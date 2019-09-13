#Implements a Least Recently Used Cache, initialized by a size. The cache supports operations Get() and Put(), each running in O(1) time.
# The cache uses a hash-table storing nodes of a double linked-list allowing O(1) time for each operation.

class DoubleNode:
    def __init__(self,val):
        self.val=val
        self.hash=0
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self,size):
        self.size=size
        self.len=0
        self.hash=0
        self.head=None
        self.tail=None
        self.ls=[]
    def AddToHead(self,val):
        if(self.head==None):
            self.head=DoubleNode(val)
            self.tail=self.head
        if(self.len==1):
            temp=DoubleNode(val)
            self.tail.prev=temp
            temp.next=self.tail
            self.head=temp
        else:
            temp=DoubleNode(val)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
        self.head.hash=self.hash
        self.hash=self.hash+1
        self.len=self.len+1
    def TailToHead(self,val):
        self.tail.next=self.head
        temp=self.tail.prev
        temp.next=None
        self.tail.prev=None
        self.head.prev=self.tail
        self.head=self.tail
        self.head.val=val
        self.head.hash=self.tail.hash
        self.tail=temp
        #self.tail.next=None
    def Retrieve(self,node):
        if(node!=self.head):
            temp=node
            node.prev.next=node.next
            temp.prev=None
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
        return node
    def Put(self,val):
        if(self.len<self.size):
            self.AddToHead(val)
            self.ls=self.ls+[self.head]
        else:
            self.TailToHead(val)
            self.ls[self.head.hash]=self.head
    def Get(self,key):
        if(key<self.size):
            if(key==self.tail.hash):
                self.TailToHead(self.ls[key].val)
                return self.ls[key].val
            rval=self.Retrieve(self.ls[key])
            return rval.val
        return -1
    def Print(self):
        i=self.head
        while(i!=None):
            print(i.val)
            i=i.next
            
    # Driver Code
    A=LRUCache(4)
A.Put(2)
A.Put(1)
A.Put(3)
A.Put(4)
A.Get(0)
A.Put(6)
A.Print()
