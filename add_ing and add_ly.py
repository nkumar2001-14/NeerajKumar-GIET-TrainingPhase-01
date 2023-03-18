str=input()
if len(str)>2:
    if str[-3:]!="ing":
        str=str+"ing"
        print(str)
    elif str[-3:]=="ing":
        str=str+"ly"
        print(str)
else:
    print(str)



