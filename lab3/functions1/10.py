def unique_list(list_1):
    list_2=[]
    for x in list_1:
        if x not in list_2:
            list_2.append(x)
    return list_2

list_1=[]
print(unique_list(list_1))