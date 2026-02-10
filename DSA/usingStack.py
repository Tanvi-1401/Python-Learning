stack = []
size = int(input("Enter stack size: "))

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peep")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # PUSH
    if choice == 1:
        if len(stack) == size:
            print("Stack Overflow! Cannot push.")
        else:
            item = int(input("Enter element to push: "))
            stack.append(item)
            print(item, "pushed into stack")

    # POP
    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow! Cannot pop.")
        else:
            popped = stack.pop()
            print("Popped element:", popped)

    # PEEP / PEEK
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Top element is:", stack[-1])

    #Display
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(len(stack)-1, -1, -1):
                print(stack[i])

    # EXIT
    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
