def find33(list):
 list=int(input())
 for i in range(len(list)-1):
    if list[i] == 3 and list[i+1] == 3:
        return True
 else:
    return False
 
find33(list)