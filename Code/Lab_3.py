print("Welcome to the Flarsheim Guesser!")

guess = True

while guess == True: 
    remainder1 = -1
    while remainder1 < 0 or remainder1 > 2:
        print("Please think of a number between and including 1 and 100")
        remainder1 = int(input('What is the remainder when your number is divided by 3? '))
        if remainder1 < 0:
            print("The value entered must be 0 or greater")
        elif remainder1 > 3: 
            print("The value entered must be less than 3")
        else: 
            break
    remainder2 = int(input("What is the remainder when your number is divided by 5? ")) 
    remainder3 = int(input("What is the remainder when your number is divided by 7? "))
    for num in range(0,101):
        if (num % 3 == remainder1) and (num % 5 == remainder2) and (num % 7 == remainder3):
            print(num)
    user_input = input("Do you want to play again? Y to continue, N to quit  ==> ")
    if user_input == 'n' or 'N':
        guess = False



    
    
        

