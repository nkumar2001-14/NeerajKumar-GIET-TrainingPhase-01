#Find the number of subarrays in an array of postion integers such that sum of the
#subarray is an odd integer, two subarray are considered different if they start or
#end at different index input..
#1
#3
#[1 2 3]
#[1] [1 2] [1,2,3] [2] [2,3] [3]
#4
#n1=int(input())
#n2=int(input())
'''l1=[]
l2=[]
for i in range(n1,n2+1):
    l1.append(i)
print(l1)
array=[i for i in range(n1,n2+1)]
print(array) 
l1=[array[i:j+1] for i in range(len(array)) for j in range(i,len(array))]
print(l1)
c=0
for i in l1:
    if sum(i)%2!=0:
        c+=1
print(c)

result=[]
for i in range(len(array)):
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
result=[array[i:j+1] for i in range(len(array))
        for j in range(i,len(array))]
print(result)
'''




#For loop version
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else:
        result.append(i**2)
print(result)


#List Comprehension

print([i if i%2!=0 else i**2 for i in range(11)  ])
