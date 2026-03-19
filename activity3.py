print("Select your ride: ")
print("1. Bike")
print("2. Car")
choice = int( input("Enter your choice: "))
if( choice == 1):
    print("What type of bike do you want: ")
    print("1. Triumph\n")
    print("2. Royal Enfield\n")
    choice2=int(input("Enter your choice2: "))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")

elif( choice==2 ):
    print("What type of car?")
    print("1.Lambourgini")
    print("2.Mercedes")
    choice3=int(input("Enter your choice3: "))
    if choice3==1:
        print("You have selected Lambourgini")
    else:
        print("You have selected Mercedes")
    
else:
    print("Wrong Choice!")