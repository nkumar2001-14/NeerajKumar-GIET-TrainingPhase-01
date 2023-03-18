#FUNCTIONS
#1.Positional Arguements
'''def f1():
    print("It's a function..")
f1()
def f2(n1,n2):
    n3=n1+n2
    return n3
    #print("n1:",n1,"n2:",n2)
print(f2(1,2))
def f3(n1,n2):
    n3=n1+n2
    return n3
print(f3(1,2.7))
def f4(n1,n2):
    n3=n1+str(n2)
    return n3
print(f4("1",2.7))
#2.Keyword Arguements
def f5(n1,n2,n3,n4):
    print("n1=",n1,"n2=",n2,"n3=",n3,"n4=",n4)
f5(n4="1",n3=2.7,n2=10,n1=23)
#3.Default Arguements
def fun(name,rollno,branch="CSE",cname="GIET"):
    print(name,rollno,branch,cname)
fun("Neeraj",54,"CST")
fun("Mohit",5)
fun("Nikhil",4,"CST")
fun("Monu",1)
fun("Nikhil",4,"CST")
fun("Monu",1,"ECE")
#4. Variable
def fun(*var): #tuple
    for i in var:
        print(i)

fun(1,2)
print()
fun(1,2,3)
print()
fun(1,2,3,4,5,6,7)
print()'''
#####SAME
'''def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    print(sum)
    
add(1,2)
print()
add(1,2,3)
print()
add(1,2,3,4,5,6,7)
print()
-------------------------
def add(*var):
    sum=0
    for i in var:
        sum=sum+i
        print(sum)
    
add(1,2)
print()
add(1,2,3)
print()
add(1,2,3,4,5,6,7)
print()
------------------------
def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return sum
    
print(add(1,2))
print()
print(add(1,2,3))
print()
print(add(1,2,3,4,5,6,7))
print()'''
###
