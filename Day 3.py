#!/usr/bin/env python
# coding: utf-8

# In[11]:


#for loop --element odd-->Square it
#if --element even -->cube it
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print([[j**3 if j%2==0 else j**2 for j in i] for i in mat])


# In[8]:


mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
res=[]
for i in mat:
    row_data=[]
    for j in i:
        if j%2==0:
            row_data.append(j**3)
        else:
            row_data.append(j**2)
    res.append(row_data)
print(res)


# In[25]:


mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
result=[]
#result1=[]
for i in listb:
    for j in mylist:
        if j==i:
            result.append((j,mylist.index(i)))
            #result1.append(i)
        else:
            j+=1
print(result)
#print(result1)
#print(result.append(result1))
                           


# In[26]:


mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
print([(i ,mylist.index(i)) for i in listb])


# In[35]:


mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
result={}
for i in listb:
    result.update({i:mylist.index(i)})
print(result)


# In[30]:


mylist=[9,3,6,1,5,0,8,2,4,7]
listb=[6,4,6,1,2,2]
print({i :mylist.index(i) for i in listb})


# In[41]:


sentences=["a new world record was set","in the holy city of Ayodhya","on the eve of diwali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of saryu river"]
stopwords=['for','a','of','the','and','to','in','on','with','was']
result=[]
for sentence in sentences:
    row_data=[]
    for word in sentence.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)
print([[word for word in sentence.split() if word not in stopwords]for sentence in sentences])


# In[44]:


array=list(map(int,input().split(",")))
num1=sum(array[:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1)
    


# In[50]:


#STRING ROTATION
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    stt.append(s1)
    num.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))
    


# In[1]:


def find_factors(num):
    factors=[]
    for i in range (2,(num+1)):
        if num%i==0:
            factors.append(i)
    return 


# In[ ]:




