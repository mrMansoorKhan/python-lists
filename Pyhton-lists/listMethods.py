list = [4, 6, 3, 7, 9]

list.append(2) #adds at the end
print(list)

print(list.sort())#prints none
list.sort()
print(list)


list.sort(reverse=True)
list.reverse() #reverses list
# list.insert(idx,el)
list.insert(3,10)

list.remove(6)#remove 1st occurrence 
#list.pop(idx)
list.pop(0)