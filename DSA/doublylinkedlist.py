class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new=Node(data)
        if self.head:
            self.head.prev=new
            new.next=self.head
        self.head=new

    def insert_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        
        temp=self.head
        while temp.next:
            temp=temp.next
        
        temp.next=new
        new.prev=temp

    def insert_pos(self,pos,data):
        new=Node(data)
        temp=self.head
        
        for i in range(pos-1):
            temp=temp.next
        
        new.next=temp.next
        new.prev=temp
        
        if temp.next:
            temp.next.prev=new
        
        temp.next=new

    def delete_begin(self):
        if self.head:
            self.head=self.head.next
            if self.head:
                self.head.prev=None

    def delete_end(self):
        temp=self.head
        
        while temp.next:
            temp=temp.next
        
        temp.prev.next=None

    def delete_pos(self,pos):
        temp=self.head
        
        for i in range(pos):
            temp=temp.next
        
        temp.prev.next=temp.next
        
        if temp.next:
            temp.next.prev=temp.prev

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.next
        print("None")


dl=DoublyList()

while True:

    print("\n1.Insert Begin")
    print("2.Insert End")
    print("3.Insert Position")
    print("4.Delete Begin")
    print("5.Delete End")
    print("6.Delete Position")
    print("7.Display")
    print("8.Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        x=int(input("Enter value: "))
        dl.insert_begin(x)

    elif ch==2:
        x=int(input("Enter value: "))
        dl.insert_end(x)

    elif ch==3:
        pos=int(input("Position: "))
        x=int(input("Value: "))
        dl.insert_pos(pos,x)

    elif ch==4:
        dl.delete_begin()

    elif ch==5:
        dl.delete_end()

    elif ch==6:
        pos=int(input("Position: "))
        dl.delete_pos(pos)

    elif ch==7:
        dl.display()

    elif ch==8:
        break