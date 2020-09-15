import random
print("This is a dice stimulator")
z = "y"
x = random.randint(1,6)

while z == "y":
    x = random.randint(1,6)

    if(x==1):
        print ("|       |")
        print ("|   *   |")
        print ("|       |")
        print ("|       |")
    if(x==2):
        print ("|       |")
        print ("|  * *  |")
        print ("|       |")
        print ("|       |")
    if(x==3):
        print ("|       |")
        print ("|   *   |")
        print ("|  * *  |")
        print ("|       |")
    if(x==4):
        print ("|       |")
        print ("|  * *  |")
        print ("|  * *  |")
        print ("|       |")
    if(x==5):
        print ("|   *   |")
        print ("|  * *  |")
        print ("|  * *  |")
        print ("|       |")
    if(x==6):
        print ("|       |")
        print ("|  * *  |")
        print ("|  * *  |")
        print ("|  * *  |")
    z = input("press y to roll again ")
