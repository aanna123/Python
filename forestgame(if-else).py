
print('\tPlay game \n\tExit')
choice=input("enter your choice: ")
if choice =="Play game" or "play game":
    print("Welcome to the Forest Game!!!!!")
    choice=input("Do you wanna enter the forest??\t \t \t Yes or No???\n")
    if choice=="yes":
        print("You are inside the Great amazon forest\n") 
        choice=input("take left or right??\n")
        if choice=="left":
            choice=input("OH goddd there is a riverrrr!! \n We have to cross the river,but we have a problemmm, there are ALIGATORS,\n \n \t what do we do? \n fight or run??\n")
            if choice=="fight":
                print("victoryyy we have won against the gatorr\n\t YOU WIN") 
                exit()
            else:
                print("my bad you became prey to the gators,extra protein i guess!")
                exit()
        else:
            choice=input("Ooopsssieee, I think the king of the forest wants to have a friendly game\n\t fight or run??\n")
            if choice=="fight":
                print("OMG you have defeated the king you shall be the king from now on\n\t Congratulations your majesty!!! ")
                exit()
    else: 
        print("\t \tGAME-OVER    -_-") 
        exit()
else:
    print("See you later buddy!!")



