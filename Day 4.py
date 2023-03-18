#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Nearest_Palindrome
import sys
def nearest_palindrome(num):
    numstr=str(num)
    for i in range(num+1,sys.maxsize):
        if str(i)==str(i)[::-1]:
            return i
print(nearest_palindrome(99))
print(nearest_palindrome(1221))


# In[21]:


#Medical Speciality
def max_visited_speciality(patient_list,medical_speciality):
    max_visit=0
    P=patient_list.count('P')
    E=patient_list.count('E')
    O=patient_list.count('O')
    if P>E and P>O:
        Speciality=medical_speciality['P']
    elif E>O and E>P:
        Speciality=medical_speciality['E']
    else:
        Speciality=medical_speciality['O']
    return Speciality
patient_list=[101,'P',102,'O',202,'O',305,'P']
medical_speciality={'P':'Pediatrics','O':'Orthopedics','E':'Ent'}
Speciality=max_visited_speciality(patient_list,medical_speciality)
print(Speciality)


# In[39]:


str1="I like Python"
str2="Java is very popular language"
res=[]
for i in str1:
    for j in str2:
        if (i==j and i!=' ' and j!=' '):
            res.append(j)
            break
if(len(res)==0):
    print("-1")
for i in res:
    print(i,end='')
    


# In[54]:


class abc:
    def __init__(self,num1):
        self.num=num1
    def set_num(self,num2):
        self.num=num2
    def get_num(self):
        return self.num
obj=abc(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())


# In[48]:


class abc:
    def __init__(self,id):
        self.id=100
c1=abc(200)
print(c1.id)


# In[53]:


class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Let us C"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"
print(my_fav.title)
print(your_fav.title)


# In[61]:


class shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
s1=shoe(1000,"canvas")
print("Unique ID",id(s1))#id will change everytime


# In[62]:


class shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material
    def __str__(self):
        return "Shoe with price:" +str(self.price)+" and material:"+self.material
s1=shoe(1000,"canvas")
print(s1)


# In[66]:


class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying Details")
    def purchase(self):
        self.display()
        print("Calculating Price")
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
m1=m2
print(m1)
print(m2)


# In[70]:


class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.totalPrice=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.totalPrice=self.price-self.price*(discount/100)
        print("Total Price",self.brand,"Mobile is",self.totalPrice)
    def AmountReturn(self):
        return (self.price-self.totalPrice)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
mob1.AmountReturn()
mob2.AmountReturn()


# In[85]:


class Customer:
    def __init
    __(self,cust_id,name,age,wallet_balance):
        self.cust_id=cust_id
        self.name=name
        self.age=age
        self.__wallet_balance=wallet_balance
    def set_balance(self,amount):
        if amount<50000 and amount >0:
            self.__wallet_balance+=amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"Neeraj",22,1000)
print(c1.get_wallet_balance())
#c1.update_balance(500)
#c1.show_balance()
c1.set_balance(5000)
print(c1.get_wallet_balance())


# In[87]:


class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam length:",dam1.get_length())


# In[88]:


class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self,glass_top,wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self,glass_top,wooden_top):
        self.assign_data(glass_top,wooden_top)
        if (self.__glass_top==True):
            rate=20000
        elif(self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate(False,True)
print(rate)


# In[2]:


class Table:
    def __init__(self):
        print(id(self))
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
dining_table=Table()
#print(id(dining_table))
back_table=Table()
#print(id(back_table))
front_table=back_table
#print(id(front_t

back_table=dining_table
print(id(dining_table),id(back_table),id(front_table))


# In[ ]:




