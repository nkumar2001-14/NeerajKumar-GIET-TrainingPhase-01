marks=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average(marks):
    sum1=0
    c=0
    for i in marks:
        sum1=sum1+i
    avg1=sum1/len(marks)
    for i in marks:
        if i>avg1:
            c+=1
    percent=(c/len(marks))*100
    return percent

def sort_marks(marks):
    marks=sorted(marks)
    return marks
def generate_frequency():
    freq=[]
    for x in range(26):
        c=0
        for y in marks:
            if x==y:
                c+=1
        freq.append(c)
    return freq
print(find_more_than_average(marks))
print(generate_frequency())
print(sort_marks(marks))  
