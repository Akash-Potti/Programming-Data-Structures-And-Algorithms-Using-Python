#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WEEK 1 PROGRAMMING ASSIGNMENT


# In[2]:


#1)
#A positive integer m is a prime product if it can be written as p×q, where p and q are both primes. .
#Write a Python function primeproduct(m) that takes an integer m as input and returns True if m is a prime product and False otherwise. (If m is not positive, your function should return False.)

def primeproduct(m):
    def is_prime(n):
        if n<=1:
            return False
        
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    
    if m<=0:
        return False
    
    for i in range(2,m):
        if m%i==0:
            if is_prime(i) and is_prime(m//i):
                return True
        return False


# In[3]:


#2)
#Write a function delchar(s,c) that takes as input strings s and c, where c has length 1 (i.e., a single character), and returns the string obtained by deleting all occurrences of c in s. If c has length other than 1, the function should return s
def delchar(s,c):
    a=""
    if len(c)==1:
        for i in range(len(s)):
            if c not in s[i]:
                a+=s[i]
  
            else:
                continue
    elif len(c)>1:
        return s
    return a


# In[4]:


#3)
#Write a function shuffle(l1,l2) that takes as input two lists, 11 and l2, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

def shuffle(l1,l2):
    l3=[]
    for i in range(0,max(len(l1),len(l2))):
         if i<len(l1):
            l3.append(l1[i])
        
         if i<len(l2):
            l3.append(l2[i])
    return l3


# In[5]:


#WEEK 3 PROGRAMMING ASSIGNMENT


# In[6]:


#1)
#Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.

def expanding(l):
    diff=l[1]-l[0]
    
    for i in range(2,len(l)):
        if abs(l[i]-l[i-1])>diff:
            diff=abs(l[i]-l[i-1])
        else:
            return False
    return True


# In[7]:


#2)
#Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

def sumsquare(l):
    l2=[]
    even_square=0
    odd_square=0
    for i in range(0,len(l)):
        if l[i]%2==0:
            even_square=even_square+l[i]**2
        elif l[i]%2!=0:
            odd_square=odd_square+l[i]**2
    l2.insert(0,odd_square)
    l2.insert(1,even_square)
    return l2


# In[8]:


#3)
#A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. 
#A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. 
def transpose(m):
    num_rows=len(m)
    num_coloumns=len(m[0]) if m else 0
    
    transposed_matrix=[[0 for n in range(num_rows)] for m in range(num_coloumns)]
    
    for i in range(num_rows):
        for j in range(num_coloumns):
            transposed_matrix[j][i]=m[i][j]
    return transposed_matrix


# In[ ]:




