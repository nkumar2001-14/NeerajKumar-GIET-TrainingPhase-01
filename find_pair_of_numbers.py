def find_pairs_of_numbers(lst,n):
    c=0
    for x in lst:
        index=lst.index(x)+1
        for y in range(index,len(lst)):
            if x+lst[y]==n:
                c+=1
    return c
    
lst=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(lst,n))
'''
lst=[]
n=int(input())

c=0
for x in lst:
    index=lst.index(x)+1
    for y in range(index,len(lst)):
        if x+lst[y]==n:
            c+=1
    print(c)'''
