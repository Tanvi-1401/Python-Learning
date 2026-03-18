class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new=Node(data)

        if self.head is None:
            self.head=new
            new.next=self.head
            return

        temp=self.head
        while temp.next!=self.head:
            temp=temp.next

        new.next=self.head
        temp.next=new
        self.head=new

    def insert_end(self,data):
        new=Node(data)

        if self.head is None:
            self.head=new
            new.next=self.head
            return

        temp=self.head
        while temp.next!=self.head:
            temp=temp.next

        temp.next=new
        new.next=self.head

    def insert_pos(self,pos,data):
        new=Node(data)
        temp=self.head

        for i in range(pos-1):
            temp=temp.next

        new.next=temp.next
        temp.next=new

    def delete_begin(self):
        if self.head is None:
            return

        temp=self.head
        while temp.next!=self.head:
            temp=temp.next

        self.head=self.head.next
        temp.next=self.head

    def delete_end(self):
        temp=self.head

        while temp.next.next!=self.head:
            temp=temp.next

        temp.next=self.head
        
    def delete_pos(self,pos):

        if self.head is None:
            print("List empty")
            return

        if pos == 1:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            self.head=self.head.next
            temp.next=self.head
            return

        temp=self.head
        for i in range(pos-2):
            temp=temp.next

        temp.next=temp.next.next    

    def display(self):
        if self.head is None:
            return

        temp=self.head
        while True:
            print(temp.data,end=" -> ")
            temp=temp.next
            if temp==self.head:
                break
        print("(back to head)")


cl=CircularList()

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
        cl.insert_begin(x)

    elif ch==2:
        x=int(input("Enter value: "))
        cl.insert_end(x)

    elif ch==3:
        pos=int(input("Position: "))
        x=int(input("Value: "))
        cl.insert_pos(pos,x)

    elif ch==4:
        cl.delete_begin()

    elif ch==5:
        cl.delete_end()

    elif ch==6:
        pos=int(input("Position: "))
        cl.delete_pos(pos)
    
    elif ch==7:
        cl.display()

    elif ch==8:
        break