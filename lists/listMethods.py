list = [6, 8, 20]

list.append(10)
print(list)

#print(list.sort()) -- output null
list.sort()
print(list)
list.sort(reverse = True)
print(list)

list.reverse()
print(list)

list.insert(2,7) # (indx,el)
print(list)

list.remove(8)
print(list)

list.pop(1)
print(list)