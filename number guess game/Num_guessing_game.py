import random
print("Welcome to number guessing game ")
print(" HINT :Enter the upperlimit as low as possible to nail the game! ")
upper_limit=int(input("Enter the upperlimit "))
lower_limit =int(input("Enter the lowerlimit "))
random_int=random.randint(lower_limit,upper_limit)
print("You have to choose a number between ",lower_limit ,"and",upper_limit)
chances=0
while(chances<5):
    guess=int(input("enter the number "))
    if(guess==random_int):
        print("Your guess is correct ")
        break
    elif(guess>random_int):
        print("Your guess should be little higher ")
        chances+=1
    elif(guess<random_int):
        print("Your guess should be little lower ")
        chances+=1
    if(chances==4):
        print(" This is your last chance ")
        print("ALL THE BEST BUDDY ")
    if(chances==7):
        print("You have runout of chances ")
        print("The number is ",random_int)
        print("Better luck next time ")
        break




