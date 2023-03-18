def fun(str):
    if len(str)<2:
        return -1
    else:
        return str[0:2]+str[-2:]

print(fun("w3resource"))
print(fun("w3"))
print(fun("A"))
