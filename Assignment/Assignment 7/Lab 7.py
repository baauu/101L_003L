## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 6 
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/ 
##  unknown Caesar key. 
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##    
##  Crack(string_text): Decrypts a string by repeatedly calling Decrypt with each 
##    possible key (1 to 25) and remembering the one with a letter frequency 
##    closest to English based on counts of E, T, O, A, I, N. Returns tuple: 
##    decrypted string and decryption key. 
##    
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
  
################################ 

import string 

#Encryption function ; completed 
def Encrypt(string_text, int_key):
    '''Caesar-encrypts string using specified key.'''
    if string_text.isupper() == True:
        for letter in string_text: 
            string_order = ord(letter)
            shift_number = string_order + int_key
            if string_order == 32:
                shift_number -= int_key
            elif shift_number > 90:
                shift_number = 64+(shift_number % 122)
            crypt = chr(shift_number)
            print(crypt, end = '')
    if string_text.islower() == True: 
        for letter in string_text: 
            string_order = ord(letter)
            shift_number = string_order + int_key
            if string_order == 32:
                shift_number -= int_key
            elif shift_number > 122: 
                shift_number = 96 + (shift_number % 122)
            crypt = chr(shift_number)
            new_crypt = crypt.upper()
            print(new_crypt, end = '')

#Decrypted function ; completed 
def Decrypt(string_text, int_key):
    ''' Decrypts Caesar-encrypted string with specified key. '''
    if string_text.islower() == True:
        for letter in string_text:
            string_order = ord(letter)
            shift_number = string_order - int_key
            if string_order == 32:
                shift_number += int_key
            elif shift_number < 65: 
                shift_number = 91 - (shift_number % 65)
            crypt = chr(shift_number)
            new_crypt = crypt.upper()
            print(new_crypt, end = '')

#Main Menu
def print_menu():
    '''Prints menu. No user interaction. '''
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')

#Input
def get_input():
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''
    button = input('Enter your selection ==> ')
    return button


    
#Main program
def main(option):
    turn = True
    while turn == True:
        if option == '1':
            message = input('Enter (brief) text to encrypt: ')
            shift = int(input('Enter the number to shift letters by: '))
            print('Encrypted: ')
            Encrypt(message, shift)
            print()
            print()
            break
        elif option == '2':
            message = input('Enter (brief) text to encrypt: ')
            shift = int(input('Enter the number to shift letters by: '))
            print('Decrypted: ')
            Decrypt(message, shift)
            print()
            print()
            break
        elif option == 'Q':
            turn = False
            break
    
#Program 
game = True
while game == True:
    print_menu()
    selection = get_input()
    if selection == 'Q':
        game = False
        break
    main(selection)
    print()

