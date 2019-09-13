# A BST is created with all relevant functions. Will be used further to create an AVL tree.

class BSTNode:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
    def Add(self,val):
        if(val<self.val and (self.left==None)):
            self.left=BSTNode(val)
            return 0
        if(val>=self.val and (self.right==None)):
            self.right=BSTNode(val)
            return 0
        else:
            if(val<self.val):
                self.left.Add(val)
            if(val>=self.val):
                self.right.Add(val)
    def AddNode(self,node):
        if(node.val<self.val and (self.left==None)):
            self.left=node
            return 0
        if(node.val>=self.val and (self.right==None)):
            self.right=node
            return 0
        else:
            if(node.val<self.val):
                self.left.AddNode(node)
            if(node.val>=self.val):
                self.right.AddNode(node)
    def Find_Smallest_Leaf(self):
        if(self.left!=None):
            return self.left.Find_Smallest_Leaf()
        if(self.left==None):
            if(self.right==None):
                return self.val
                #self.val=None
            else:
                return self.right.Find_Smallest_Leaf()
    def Find_Largest_Leaf(self):
        if(self.right!=None):
            return self.right.Find_Largest_Leaf()
        if(self.right==None):
            if(self.left==None):
                return self.val
                #self.val=None
            else:
                return self.left.Find_Smallest_Leaf()
    
    def InOrder(self):
        if(self.left!=None):
            self.left.InOrder()
        if(self.val!=None):
            print(self.val)
        if(self.right!=None):
            self.right.InOrder()   
    def PreOrder(self):
        if(self.val!=None):
            print(self.val)
        if(self.left!=None):
            self.left.PreOrder()
        if(self.right!=None):
            self.right.PreOrder()
    def PostOrderHelp(self,ls):
        if(self.left!=None):
            ls=self.left.PostOrderHelp(ls)
        if(self.right!=None):
            ls=self.right.PostOrderHelp(ls)
        if(self.val!=None):
            ls=ls+[self.val]
        return ls
    def PostOrder(self):
        return self.PostOrderHelp([])
    def PrintHelper(self,accum):
        if(self.val!=None):
            print(accum*" "+str(self.val))
        if(self.left!=None):
            self.left.PrintHelper(accum+1)
        if(self.right!=None):
            self.right.PrintHelper(accum+1)
    def Print(self):
        return self.PrintHelper(0)
    def search(self,val):
        if(((self.left==None) and val<self.val) or ((self.right==None) and val>self.val)):
            return [False,[]]
        if(self.val==val):
            return [True,self]
        else:
            if(val<self.val):
                return self.left.search(val)
            else:
                return self.right.search(val)
    def HeightHelp(self,h):
        if((self.right==None) and (self.left==None)):
            return h
        if(self.left==None):
            return self.right.HeightHelp(h+1)
        if(self.right==None):
            return self.left.HeightHelp(h+1)
        else:
            if(self.left.HeightHelp(h+1)>self.right.HeightHelp(h+1)):
                return self.left.HeightHelp(h+1)
            else:
                return self.right.HeightHelp(h+1)
    def Height(self):
        ls=[]
        if(self.left!=None):
            ls=ls+[self.left.HeightHelp(1)]
        else:
            ls=ls+[0]
        if(self.right!=None):
            ls=ls+[self.right.HeightHelp(1)]
        else:
            ls=ls+[0]
        return ls
    def isBalanced(self):
        if(abs(self.Height()[0]-self.Height()[1])>1):
            return False
        else:
            return True
    def LoD_Helper(self,ls,depth):
        if(self.left!=None):
            ls=self.left.LoD_Helper(ls,depth+1)
        if(self.right!=None):
            ls=self.right.LoD_Helper(ls,depth+1)
        ls=ls+[depth]
        return ls
    def LoD(self):
        ls1=[]
        ls2=[]
        rval=[]
        for i in range(0,self.HeightHelp(0)+1):
            rval=rval+[LinkedList()]
        ls1=self.LoD_Helper(ls1,0)
        ls2=self.PostOrder()
        for i in range(0,len(ls1)):
            rval[ls1[i]].AddToTail(ls2[i])
        return rval
class BST:
    def __init__(self,val):
        self.root=BSTNode(val)
        self.values=[val]
    def ADD(self,val):
        self.root.Add(val)
        self.values=self.values+[val]
    def IN_ORDER(self):
        return self.root.InOrder()
    def PRE_ORDER(self):
        return self.root.PreOrder()
    def POST_ORDER(self):
        return self.root.PostOrder()
    def PRINT(self):
        return self.root.Print()
    def SEARCH(self,val):
        return self.root.search(val)
    def HEIGHT(self):
        return self.root.Height()
    def IS_BALANCED(self):
        return self.root.isBalanced()
    def BFS(self):
        return self.root.LoD()
    def GET_RANDOM_NODE(self):
        rval=self.SEARCH(self.values[len(self.values)-1])[1]
        self.values=self.values[1:]+[self.values[0]]
        return rval
    def FIND_SMALLEST_LEAF(self):
        return self.root.Find_Smallest_Leaf()
    def FIND_LARGEST_LEAF(self):
        return self.root.Find_Largest_Leaf()

def CONV_ARRAY_TO_BST_HELPER(tree,arr):
    if(len(arr)%2==0):
        tree.ADD(arr[int(len(arr)/2)])
        CONV_ARRAY_TO_BST_HELPER(tree,arr[0:int(len(arr)/2)])
        if((len(arr)/2)+1<len(arr)):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[int(len(arr)/2)+1:])
    else:
        tree.ADD(arr[int((len(arr)/2)-0.5)])
        if(int(len(arr)/2)-0.5>=0):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[0:int(len(arr)/2-0.5)])
        if((len(arr)/2)+0.5<len(arr)):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[int(len(arr)/2+0.5):])
            
def CONV_ARRAY_TO_BST(arr):
    if(len(arr)%2==0):
        tree=BST(arr[int(len(arr)/2)])
        CONV_ARRAY_TO_BST_HELPER(tree,arr[0:int(len(arr)/2)])
        if(int(len(arr)/2)+1<len(arr)):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[int(len(arr)/2)+1:])
    else:
        tree=BST(arr[int((len(arr)/2)-0.5)])
        if(int(len(arr)/2)-0.5>=0):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[0:int(len(arr)/2-0.5)])
        if((len(arr)/2)+0.5<len(arr)):
            CONV_ARRAY_TO_BST_HELPER(tree,arr[int(len(arr)/2+0.5):])
    return tree

def Validate_BST_Helper(tree_node):
    if(tree_node.left!=None):
        if(tree_node.left.val>tree_node.val):
            return False
    if(tree_node.right!=None):
        if(tree_node.right.val<tree_node.val):
            return False
def Validate_BST(tree_node):
    rval=Validate_BST_Helper(tree_node)
    if(rval==None):
        rval=True
    return rval

def Check_Subtree(tree1,tree2):
    val=tree1.root.search(tree2.root.val)
    if(val[0]==True):
        while(val[1].right!=None):
            if ((val[1]).PostOrder())==(tree2.root.PostOrder()):
                return True
            else:
                if((val[1]).right.val==val[1].val):
                    val=val[1].right.search(tree2.root.val)
                else:
                    break
    return False
    
