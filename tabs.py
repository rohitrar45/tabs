import os
stack = []
def insert():
    os.system("cls")
    show()
    global stack
    data = input("Enter the url\n")
    if(data in stack):
        ind = stack.index(data)
        for i in range(ind):
            stack[ind-i] = stack[ind-(i+1)]
            pass
        stack[0] = data
    else:
        stack.append(data)
def show():
    global stack
    print("YourTabs:\n", stack)
def dele():
    global stack
    print(stack.pop(), "is deleted from your tab")
    show()
cnt = 5
while cnt != 4:
    cnt = int(input("Choose anyone option\n1.Insert\n2.Show the updated tabs\n3.Delete\n4.Exit"))
    if cnt == 1:
        insert()
    elif cnt == 2:
        show()
    elif cnt == 3:
        dele()


