'''def fun(str1):
    l_c=0
    d_c=0
    for i in str1:
        if i.isalpha():
            l_c=l_c+1
        elif i.isdigit():
            d_c=d_c+1            
        else:
            continue
    return [l_c,d_c]
print(fun("Infosys 123"))'''

str1=input()
l_c=0
d_c=0
for i in str1:
    if i.isalpha():
        l_c=l_c+1
    elif i.isdigit():
        d_c=d_c+1            
    else:
        continue
print([l_c,d_c])
