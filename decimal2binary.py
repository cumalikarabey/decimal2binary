#!/usr/bin/env python
# coding: utf-8

# In[68]:


try:
    inp = int(input("Decimal number: "))
except:
    print("404 ERROR must be an integer")


# In[69]:


binary = []
while inp != 1:
    
    if inp < 0:
        inp = -1*inp
        verification = True
        
    div = int(inp//2)
    rem = inp - div*2 #finding remainder
    binary.append(rem)
    inp = div
    if inp == 1:
        binary.append(inp)
        binary = binary[::-1] #we must reverse finded numbers
        if verification == True:
            binary[0] = binary[0]*-1
            
    


# In[70]:


binary

