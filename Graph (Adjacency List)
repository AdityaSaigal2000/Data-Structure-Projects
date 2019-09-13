#Creates a representation of a graph using Adjacency Lists. A queue class is also created for BFS implementation. The graph is currently 
#unweighted (directed or undirected). Weights will be added in the next iteration to implement minimal spanning tree algorithms.

# Build_Order(projects,dep), Build_OrderH1(projects,dep) and Build_OrderH2(graph,ls,rval,depth) transform a list of projects and dependencies
# to a directed graph. A possible order of completing all projects is derived from this graph.
def Build_OrderH1(projects,dep):
    ls=[]
    graph=Graph()
    for i in projects:
        ls=ls+[Node(i)]
    for i in dep:
        for j in range(0,len(ls)):
            if(ls[j].val==i[0]):
                break
        for k in range(0,len(ls)):
            if(ls[k].val==i[1]):
                ls[j].Add_Directed(ls[k])
    for i in ls:
        graph.Add_Node(i)
    return graph

def Build_OrderH2(graph,ls,rval,depth):
    #print(depth)
    for i in ls:
        state=True
        for j in ls:
            if(path_between_nodes(graph,j,i)==True):
                state=False
                break
        if(state==True):
            if(i not in rval):
                rval=rval+[i]
    ls=[]
    for i in rval[depth:len(rval)]:
        for j in range(0,len(i.Get_Neighbors())):
            if (i.Get_Neighbors()[j] not in ls):
                ls=ls+[i.Get_Neighbors()][j]
    for i in ls:
        print(i.val)
    print("_")
    for i in rval:
        print(i.val)
    print("_")
    if(len(ls)!=0):
        rval=Build_OrderH2(graph,ls,rval,depth+len(rval[depth:len(rval)]))
    return rval

def Build_Order(projects,dep):
    graph=Build_OrderH1(projects,dep)
    if(graph.Cycle_Detection()==True):
        print("No Valid Orders.")
        return False
    rval=Build_OrderH2(graph,graph.nodes,[],0)
    for i in range (0,len(rval)):
        rval[i]=rval[i].val
    return rval
class Queue:
    def __init__(self):
        self.list=[]
    def enq(self,val):
        self.list=[val]+self.list
    def deq(self):
        rval=self.list[len(self.list)-1]
        self.list=self.list[0:len(self.list)-1]
        return rval
class Node:
    def __init__(self,val):
        self.val=val
        self.connect=[]
    def Add_Directed(self,node):
        self.connect=self.connect+[node]
    def Add_Undirected(self,node):
        self.Add_Directed(node)
        node.Add_Directed(self)
    def Get_Neighbors(self):
        return self.connect
class Graph:
    def __init__(self):
        self.nodes=[]
    def Add_Node(self,node):
        state=True
        for j in range(0,len(self.nodes)):
            if(self.nodes[j]==node):
                return False
        if(state==True):
            self.nodes=self.nodes+[node]
        for i in range (0,len(node.connect)):
            self.Add_Node(node.connect[i])
    def Del_Node(self,node):
        state=False
        for i in range(0,len(self.nodes)):
            if(self.nodes[i]==node):
                self.nodes=self.nodes[0:i]+self.nodes[i+1:len(self.nodes)]
                state=True
                break
        if(state==False):
            print("Value doesn't exist in graph.")
            return -1
        else:
            for i in range(0,len(self.nodes)):
                for j in range(0,len(self.nodes[i].connect)):
                    if(self.nodes[i].connect[j]==node):
                        self.nodes[i].connect=self.nodes[i].connect[0:j]+self.nodes[i].connect[j+1:len(self.nodes[i].connect)]
            return 0  
        
    def DFS_Helper(self,node,ls):
        state=True
        for j in range(0,len(ls)):
            if(ls[j]==node.val):
                state=False
                break
        if(state==False):
            list1=ls     
        else:
            list1=ls+[node.val]
            for i in range(0,len(node.connect)):
                list1=self.DFS_Helper(node.connect[i],list1)
        return list1
    
    def DFS(self,node):
        state=False
        for i in self.nodes:
            if(i==node):
                state=True
                break
        if(state==False):
            print("Node doesn't exist in graph.")
            return -1
        return self.DFS_Helper(node,[])
    
    def BFS(self,node):
        ls=[]
        ls1=[]
        state=False
        for i in self.nodes:
            if(i==node):
                state=True
                break
        if(state==False):
            print("Node doesn't exist in graph.")
            return -1
        q=Queue()
        q.enq(node)
        while(len(q.list)!=0):
            ls=ls+[q.deq()]
            ls1=ls1+[ls[-1].val]
            for i in (ls[-1].Get_Neighbors()):
                if((i not in q.list) and (i not in ls)):
                    q.enq(i)
        for i in range(0,len(ls)):
            ls[i]=ls[i].val
        return ls
    def Cycle_Detection(self):
        state=False
        for i in self.nodes:
            for j in self.nodes:
                if (path_between_nodes(self,i,j)==True and path_between_nodes(self,j,i)==True):
                    state=True
                    break
            if(state==True):
                break
        return state
        
    def Cycle_Detection_UndirectedH(self,node,start,arr):
        state=False
        visited=node
        if(node not in arr):
            arr=arr+[node]
            for i in node.connect:
                if(start in i.connect and start!=visited and i not in arr):
                    state=True
                    return state
                state=self.Cycle_Detection_UndirectedH(i,start,arr)
        return state
    
    def Cycle_Detection_Undirected(self):
        state=False
        for i in self.nodes:
            if(self.Cycle_Detection_UndirectedH(i,i,[])==True):
                state=True
        return state
        
    def MinSpanKruskal(self):
            
def path_between_nodes(graph,node1,node2):
    state=False
    ls=graph.BFS(node1)
    for i in ls:
        if(i==node2.val and i!=node1.val):
            state=True
            break
    if(node2.val==node1.val):
        for i in graph.nodes:
            if (i in i.connect and i.val==node1.val):
                state=True
    return state
        
def MotherNode(graph):
    mother_ls=[]
    for i in graph.nodes:
        state=True
        for j in graph.nodes:
            if(path_between_nodes(graph,i,j)==False and i!=j):
                state=False
        if(state==True):
            mother_ls=mother_ls+[i]
    return mother_ls

