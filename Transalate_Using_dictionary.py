dict1={"merry":"god","Christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
lst1=["merry","Christmas"]
def translate(dict,lst1):
    lst2=[]
    for i in lst1:
        lst2.append(dict1[i])
    return lst2
print(translate(dict1,lst1))
    
