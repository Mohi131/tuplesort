#!/usr/bin/env python
# coding: utf-8

# In[3]:


def last(n):
    return n [-1]
def sort (turples):
    return sorted (turples, key = last)

a=[(2, 5), (1, 2), (4, 4), (2, 3), (5, 1)]
print(sort(a))
    


# In[ ]:




