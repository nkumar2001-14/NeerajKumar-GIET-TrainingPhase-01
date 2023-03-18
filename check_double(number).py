num=int(input())
dub=str(num*2)
num=str(num)
#print(len(num))
#print(len(dub))
if len(num)==len(dub):
    for i in num:
        if i in dub:
            c+=1
        break
    print("True")
            
else:
    print("False")
'''def fun(num):
    n1=str(num*2)
    num=str(num)
    c=0
    for x in num:
        if x in n1:
            c+=1
        else:
            return False
    if c==len(num):
        return True
print(fun(245))
print(fun(125874))
'''
