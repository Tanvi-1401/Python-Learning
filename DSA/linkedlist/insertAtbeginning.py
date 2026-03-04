class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
        
n = int(input("Enter elements u want to enter: ")) 
head = None
next = None    

for i in range(n):
    value = int(input("Enter value: "))
    new_node = Node(value)
    
    if head is None:
        head = new_node
        tail = new_node
        
    else:
        tail.next = new_node
        tail = new_node   
    
new_value = int(input("Enter value u want to insert at beginning: "))
new_node = Node(new_value)
new_node.next = head
head = new_node      

current = head
while current is not None:
    print(current.data, end = "->")
    current = current.next
print("None")
    