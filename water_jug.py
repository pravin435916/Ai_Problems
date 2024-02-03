x = 0
y = 0
target = 2
while True:
    rule = int(input("Enter rule :"))
    if(rule == 1):
        if(x<4):
            x = 4
    if(rule == 2):
        if(y<3):
            y = 3
    if(rule == 5):
        if(x == 4):
            print("Jug A Full")
            x = 0
    if(rule == 6):
        if(y == 3):
            print("Jug B Full")
            y = 0
    if(rule  == 7):
        y = y-(4-x)
        x = 4
    if(rule  == 9):
        x+=y
        y = 0
    if(x == target and y == 0):
        print("Target Acieved ")
        print("Final Jug A:", x)
        print("Final Jug B:", y)
        break
print("Jug A:", x)
print("Jug B:", y)