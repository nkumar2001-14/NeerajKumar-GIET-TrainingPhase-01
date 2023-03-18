#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Vehicle:
    def __init__(self,vid,vtype,cost,pamount):
        self.__vid=vid
        self.__vtype=vtype
        self.__cost=cost
        self.__pamount=None
    def get_vid(self):
        return self.__vid
    def get_vtype(self):
        return self.__vtype
    def get_cost(self):
        return self.__cost
    def calculate(self,vtype):
        if self.__vtype=="Two Wheeler":
            self.__pamount=self.__cost*0.02
            return self.__pamount
        elif self.__vtype=="Four Wheeler":
            self.__pamount=self.__cost*0.06
            return self.__pamount
        else:
            print("Invalid Input")
    def set_pamount(self):
        self.__pamount=self.calculate(self.__vtype)
    def get_pamount(self):
        self.set_pamount()
        return self.__pamount
    def display(self):
        print("ID",self.get_vid())
        print("VTYPE",self.get_vtype())
        print("COST",self.get_cost())
        print("PREMIUM_AMOUNT",self.get_pamount())
v1=Vehicle(101,"Two Wheeler",55000,0)
v1.display()


# In[ ]:


class Students:
    def __init__(self,sid,marks,age):
        self.__sid=sid
        self.__marks=marks
        self.__age=age
        self.__fees=None
    def get_sid(self):
        return self.__sid
    def get_marks(self):
        return self.__marks
    def get_age(self):
        return self.__age
    
    def validate_marks(self):
        if self.__marks>0 or self.__marks<100:
            return True
        else:
            return False
    def validate_age(self):
        if age >20:
            return True
        else:
            return False
    def checked_qualifiaction(self):
        if self.validate_marks()>65 and self.validate_age()>20:
            return True
        else:
            return False
    def set_sid(self):
        return self.__sid()
    def set_marks(self):
        return self.__marks()
    def set_age(age):
        return self.__age()
    def course_fee(self):
        c_id=int(input())
        if c_id==10001:
            if self.__marks>85:
                print("C_FEES",25575-(25575*0.75))
            else:
                print("C_FEES",25575)
       
        elif c_id==1002:
            if self.__marks>85:
                print("C_FEES",15500-(15500*0.75))
            else:
                print("C_FEES",15500)
        else:
            print("Invalid input")
        
    
    def display(self):
        #print("ID",self.get_sid())
        print("MARKS",self.get_marks())
        print("AGE",self.get_age())
        self.course_fee()
s1=Students(1001,99,21)
s1.display()


# In[ ]:




