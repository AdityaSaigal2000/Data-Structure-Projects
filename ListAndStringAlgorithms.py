# This file contains some general algorithms for lists and strings.
#Converts a linked-list to a decimal number.
def conv_to_num(LinkedList):
    factor=1
    accum=0
    i=LinkedList.headval
    while(i!=None):
        accum=accum+(i.dataval)*factor
        factor=factor*10
        i=i.nextval
    return accum
#Adds numbers represented by 2 linked lists.    
def AddLinkedList(ll1,ll2):
    return conv_to_num(ll1)+conv_to_num(ll2)
    
#String Compression ALgorithm: Replaces consecutive repeating characters with a single character and number. This string is used if shorter 
# than original.
def string_compress(string):
    new_string=""
    temp=0
    val=1
    for i in range(0,len(string)):
        if(string[i]==temp):
            val=val+1
        if(temp!=0 and string[i]!=temp):
            new_string=new_string+str(temp)+str(val)
            temp=string[i]
            val=1
        if(temp==0):
            temp=string[i]
        if (i==len(string)-1):
            new_string=new_string+str(temp)+str(val)
    if(len(new_string)>len(string)):
        new_string=string
    return new_string
    
    #Detect loops in a linked-list
    def loop_detection(ll):
    i=ll.headval
    ls=[]
    while(True):
        ls=ls+[i]
        i=i.nextval
        for j in ls:
            if(i==j):
                return i.dataval
           
   #Identify intersection of linked-lists
   def intersection(ll1,ll2):
    i=ll1.headval
    j=ll2.headval
    ls=[]
    state=0
    while(i!=None):
        while(j!=None):
            if(j==i):
                ls=ls+[i.dataval]
                state=1
            j=j.nextval
        i=i.nextval
    if(state==0):
        ls=ls+[False]
    else:
        ls=ls+[True]
    return ls
