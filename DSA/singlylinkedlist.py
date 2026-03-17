class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new=Node(data)
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

    def insert_pos(self,pos,data):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.next=temp.next
        temp.next=new

    def insert_after(self,val,data):
        temp=self.head
        while temp:
            if temp.data==val:
                new=Node(data)
                new.next=temp.next
                temp.next=new
                return
            temp=temp.next

    def insert_before(self,val,data):
        if self.head.data==val:
            self.insert_begin(data)
            return
        temp=self.head
        while temp.next:
            if temp.next.data==val:
                new=Node(data)
                new.next=temp.next
                temp.next=new
                return
            temp=temp.next

    def delete_begin(self):
        if self.head:
            self.head=self.head.next

    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None

    def delete_pos(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")


ll=LinkedList()

while True:
    print("\n1.Insert Begin 2.Insert End 3.Insert Position")
    print("4.Insert After 5.Insert Before")
    print("6.Delete Begin 7.Delete End 8.Delete Position")
    print("9.Display 10.Exit")

    ch=int(input("Enter choice: "))

    if ch==1:
        x=int(input("Enter value: "))
        ll.insert_begin(x)

    elif ch==2:
        x=int(input("Enter value: "))
        ll.insert_end(x)

    elif ch==3:
        pos=int(input("Position: "))
        x=int(input("Value: "))
        ll.insert_pos(pos,x)

    elif ch==4:
        val=int(input("Insert after value: "))
        x=int(input("New value: "))
        ll.insert_after(val,x)

    elif ch==5:
        val=int(input("Insert before value: "))
        x=int(input("New value: "))
        ll.insert_before(val,x)

    elif ch==6:
        ll.delete_begin()

    elif ch==7:
        ll.delete_end()

    elif ch==8:
        pos=int(input("Position: "))
        ll.delete_pos(pos)

    elif ch==9:
        ll.display()

    elif ch==10:
        break