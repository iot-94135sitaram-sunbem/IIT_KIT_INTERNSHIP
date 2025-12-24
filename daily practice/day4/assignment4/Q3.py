def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
list1=[23,34,45,50]
list2=[35,20,60,55]
print(overlapping(list1,list2)) 
