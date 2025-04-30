#!/usr/bin/env python
# coding: utf-8

# # Taking User Input in python
# * In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable.
# * Syntax: variable=input()

# In[1]:


a=input()
print(a)


# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

# In[2]:


a=input()
print("My name is",a)


# In[3]:


a=input("Enter Your Name:")
print("My Name is",a)


# In[4]:


x=input("Enter First Number:")
y=input("Enter Second Number:")
print(x+y)


# In[5]:


x=input("Enter First Number:")
y=input("Enter Second Number:")
print(int(x)+int(y))


# In[6]:


print('Enter your name:')
x = input()
print('Hello, ' + x)


# In[7]:


b=input('Enter your name:')
print('Hello,',x)


# ### Convert User Input to a Number
# In this example, we are using the Python input() function which takes input from the user in string format converting it into an integer adding 1 to the integer, and printing it.

# In[8]:


# Taking input from the user as integer
num = int(input("Enter a number:"))
add = num + 1
# Output
print(add)


# In[9]:


a=int(input("Enter a number:"))
print(a+1)


# ### Take float input in Python:
# In this example, we are using the Python input() function which takes input from the user in string format converts it into float adds 1 to the float, and prints it.

# In[10]:


# Taking input from the user as float
num =float(input("Enter number "))
add = num + 1
# output
print(add)


# In[11]:


a=float(input("Enter a number:"))
print(a+1)


# ### Python Accept List as a input From User:
# In this example, we are taking input from the user in string format converting it into a list, and printing it.

# In[12]:


# Taking input from the user as list
li =list(input("Enter number "))
# output
print(li)


# In[13]:


a=list(input("Enter Number"))
print(a)


# ### Take User Input for Tuples and Sets:
# In this example, we are taking input from the user in string format converting it into a tuple, and printing it.

# In[14]:


# Taking input from the user as tuple
num =tuple(input("Enter number "))
# output
print(num)


# In[16]:


a=tuple(input("Enter Number"))
print(a)


# In[17]:


a=set(input("Enter Number"))
print(a)


# In[ ]:





# In[ ]:




