'''mon=float(input())
curr=input()
if curr=="Euro":
    print("Amount equivalent to money is:",mon*0.01417)
elif curr=="British Pound":
    print("Amount equivalent to money is:",mon*0.01000)
elif curr=="Australian Dollar":
    print("Amount equivalent to money is:",mon*0.02140)
elif curr=="Canadian Dollar":
    print("Amount equivalent to money is:",mon*0.02027)
else:
    print("Invalid Currency Name")'''
    

def curr_calc(INR,curr):
    if curr=="Euro":
        print(INR*0.01417)
    elif curr=="British Pound":
        print(INR*0.01000)
    elif curr=="Australian Dollar":
        print(INR*0.02140)
    elif curr=="Canadian Dollar":
        print(INR*0.02027)
    else:
        print("Invalid Currency Name")
curr_calc(12,"Euro")
curr_calc(12,"British Pound")
curr_calc(12,"Australian Dollar")
curr_calc(12,"Canadian Dollar")
