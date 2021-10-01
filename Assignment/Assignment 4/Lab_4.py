########################################################################
##
## CS 101 Lab
## Program # 4
## Name: Jessi Bautista Espino
## Email: jbr75@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

# Asks the user if they want to play again, returns False if N or NO, and True if Y or YES. Keeps asking until they respond yes '''
def play_again() -> bool:
    user_input = input("Do you want to play again? Y to continue, N to quit  ==> ")
    if user_input == 'n' or 'NO':
        game = False
    elif user_input == 'y' or user_input == 'YES':
        game = True 
    else: 
        print('You must enter Y/YES/N/NO to continue. Please try again.')



# Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have
def get_wager():
    while game is True: 
        game = False
        while wager == False: 
            wager = print('How many chips do you want to start with? ==> ')
            if wager <= 0:
                print('Too low a value, you can only choose 1 - 100 chips')
                wager = False
            elif wager >= 101: 
                print('Too high a value, you can only choose 1 - 100 chips')
                wager = False 
            else: 
                wager = True     

#Returns the result of the slot pull
def get_slot_results():
    numbers = [(random.range(0,11), random.range(0,11), random.range(0,11))]
    return numbers

# Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. 
def get_matches(reela, reelb, reelc) -> int:
    myTuple = [reela, reelb, reelc]
    mySet = set(myTuple)

    size = len(mySet)

    if size == 3:
        return 0
    elif size == 2:
        return 2
    else:
        return 3

    # [1,2,3] => (1,2,3) len() = 3 = 0
    # [1,1,2] =>  (1,2) =len () = 2 2
    #  [1,1,1] =>  (1) len() = 1 = 3

    return 0

# Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101
def get_bank() -> int:
    bank == False
    while bank == False: 

    start_with = int(input("How many chips do you want to start with? ==> "))
    if start_with >= 101:
        print('Too high a vlaue, you can only choose 1 - 100 chips')
    elif start_with <= 0:
        print('Too low a value, you can only choose 1 - 100 chips')
    
    start_with = 
    return 0


def get_payout(wager, matches):
    three_matches =
    
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    

    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()