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

"""with default input node:-
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3
"""        
 
current = head
while current is not None:
    print(current.data, end = "->" )
    current = current.next
print("None")    