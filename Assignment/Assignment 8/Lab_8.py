##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 8
##
##########################################

import math

all_test = []
all_programs = []

#printing menu
def menu_print():
    print("          Grade Menu")
    print("1 -Add Test")
    print("2 -Remove Test")
    print("3 -Clear Tests")
    print("4 -Add Assignments")
    print("5 -Remove Assignments")
    print("6 -Clear Assignments")
    print("D -Display Scores")
    print("Q -Quit")

#getting input
def user_input():
    selected = input("==> ")
    return selected

#getting average:
def finding_average(list):
    avg = sum(list) / len(list)
    return avg

#getting SD:
def standev(list):
    average = finding_average(list)
    porque = 0
    for num in list: 
        indiv = num - average
        yup = indiv * indiv 
        porque += yup
        needs_sqr = porque / len(list)
        standard = math.sqrt(needs_sqr)
    rounded = round(standard, 2)
    return rounded

#Max
def finding_max(list):
    maxii = max(list)
    return maxii

#Min
def finding_min(list):
    minn = min(list)
    return minn

#Weighted Score:
def weighted(list_test, list_assign):
    avg_test = finding_average(list_test) 
    avg_assign = finding_average(list_assign)
    test_score = (avg_test * 0.6) + (avg_assign * 0.4)
    return test_score

#providing selection
def display(num):
    while num != 'q' or num != 'Q':
        if num == '1':
            #Adding new Test
            new_test = float(input("Enter the new Test score 0-100 ==> "))
            while new_test <= 0:
                print("New test has to be greater than zero.")
                new_test = float(input("Enter the new Test score 0-100 ==> "))
            else:
                all_test.append(new_test)
                break

        elif num == '2':
            #Remove Test
            remove_test = float(input("Enter the Assignment to remove 0-100 ==> "))
            if remove_test not in all_test:
                print("Could not find test score.")
            else:
                all_test.remove(remove_test)
            break

        elif num == '3':
            #Clearing Tests
            all_test.clear()
            print("Tests have been cleared.")
            break

        elif num == '4':
            #Add assignment
            new_assignment = float(input("Enter the new Assignment score 0-100 ==> "))
            while new_assignment <= 0:
                print("Assignment must be greater than zero.")
                new_assignment = input("Enter the new Assignment score 0-100 ==> ")
            else:
                all_programs.append(new_assignment)
            break

        elif num == '5':
            #Remove Assignment
            remove_assign = float(input("Enter the Assignment to remove 0-100 ==> "))
            if remove_assign not in all_programs:
                print("Could not find that score to remove")
            else:
                all_programs.remove(remove_assign)
            break

        elif num == '6':
            #Clear Assignments
            all_programs.clear()
            print("Assignments have been cleared.")
            break

        elif num == 'D' or num == 'd':
            number_t = len(all_test)
            number_p = len(all_programs)
            not_found = "n/a"
            print("Type               #       min       max       avg       std")
            print("=" * 60)
            if len(all_test) == 0:
                print("Tests              {}       {}        {}        {}        {}".format(number_t, not_found, not_found, not_found, not_found))
            else:
                print("Tests              {}      {}       {}       {}       {}".format(number_t, finding_min(all_test), finding_max(all_test), finding_average(all_test), standev(all_test)))
            
            if len(all_programs) == 0:
                print("Programs           {}       {}        {}        {}        {}".format(number_p, not_found, not_found, not_found, not_found))
            else: 
                print("Programs           {}      {}       {}       {}       {}".format(number_p, finding_min(all_test), finding_max(all_test), finding_average(all_test), standev(all_programs)))
            
            print()
            score = weighted(all_test, all_programs)
            print("The weighted scores is       {0:.2f}".format(score))
            break
        elif num == "Q" or num == "q":
            break

#Main program~~~~~
if __name__ == "__main__":
    game = True
    while game == True:
        print()
        menu_print()
        option = user_input()
        print()
        display(option)
        if option == "q" or option == "Q":
            game = False
            break
"""        else:
            continue"""



