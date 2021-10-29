########################################################################
##
## CS 101 Lab
## Program # 6
## Name: Jessi Bautista Espino
## Email: jbr75@umsystem.edu
##
## PROBLEM : 
##
## ALGORITHM : 
##      Provided below 
## 
## ERROR HANDLING:
##      None found. 
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import string

def school(num):
    if num[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif num[5] == '2':
        return 'School of Law'
    elif num[5] == '3':
        return 'College of Arts and Sciences'
    return 'Invalid School'


def grade(num):
    if num[6] == '1':
        return 'Freshman'
    elif num[6] == '2':
        return 'Sophomore'
    elif num[6] == '3':
        return 'Junior'
    elif num[6] == '4':
        return 'Senior'
    return 'Invalid Grade'

def character_value(num):
    if num == '0' or num == ' 1' or num == '2' or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num == '9':
        return int(num)
    else: 
        return string.ascii_uppercase.find(num)

def digitcheck(num):
    sumone = 0
    for index in range(9):
        charone = num[index]
        sumone += character_value(charone) * (index + 1)
    result = sumone % 10
    return result


def verifydigit(num):
        if len(num) != 10:
            return False, 'The length of the number given must be 10'
        elif num[0].isalpha() == False:
            return False, 'The first 5 characters must be A-Z, the invalid character is at 0 is ' + num[0]
        elif num[1].isalpha() == False: 
            return False, 'The first 5 characters must be A-Z, the invalid characters is at 1 is ' + num[1]
        elif num[2].isalpha() == False:
            return False, 'The first 5 characters must be A-Z, the invalid character is at 2 is ' + num[2]
        elif num[3].isalpha() == False:
            return False, "The first 5 characters must be A-Z, the invalid character is at 3 is " + num[3]
        elif num[4].isalpha() == False:
            return False, "The first 5 characters must be A-Z, the invalid character is at 4 is " + num[4]
        elif int(num[9]) != digitcheck(num):
            return False, "Check Digit " + num[9] + " does not match calculated value " + str(digitcheck(num))
        elif num[5] != '1' and num[5] != '2' and num[5] != '3':
            return False, "The sixth character must be 1 2 or 3"
        elif num[6] != '1' and num[6] != '2' and num[6] != '3' and num[6] != '4':
            return False, "The seventh character must be 1 2 3 or 4"
        else:
            return True, ""

if __name__ == "__main__":

    print('{:^60}'.format('Linda Hall'))
    print('{:^60}'.format('Library Card Check'))
    print('='*60)

    while True:

        print()
        num = input('Enter Library Card. Hit Enter to Exit ==> ').upper().strip()
        if num == "": 
            break
        result, error = verifydigit(num)
        if result == True: 
            print('Library card is valid.')
            print('The card belongs to a student in {}'.format(school(num)))
            print('The card belongs to a {}'.format(grade(num)))
        else:
            print('Library card is invalid')
            print(error)

