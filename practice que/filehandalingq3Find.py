def check_for_word():
    word = "learning"
    with open("practice que/practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
         print("Found")
        else:
            print("Not Found")
            
check_for_word()