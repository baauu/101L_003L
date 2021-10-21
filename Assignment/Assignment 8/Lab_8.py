##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 8
##
##########################################

#Opening a file
def open_file(prompt, mode='r'):
    while True:
        try:
            filename = input(prompt)
            file = open(filename, 'r')
            return file
        except FileNotFoundError:
            print('Could not open file {}'.format(filename))
        except IOError:
            print('There is an IO Error {}'.format(filename))

#Getting minnimum MPG
def get_min_mpg():
    while True:
        try:
            min_mpg = float(input('Enter the minimum mpg ==> '))
            if min_mpg < 0:
                print('Fuel economy must be greater than 0')
            elif min_mpg > 100:
                print('Fuel economy must be less than 100')
            else:
                return min_mpg
        except ValueError:
            print('You must enter a number for the fuel economy')
    
#The main program: 
mpg = get_min_mpg()
print()
file = open_file('Enter the name of the input vehicle file ==> ')
print()
file.readline()
out = open_file('Enter the name of the file to output to ==> ', 'w')
for line in file:
    try:
        values = line.split('\t')
        if float(values[7]) >= mpg:
            out.write('{:<40} {:<40} {:<40} {:>10.3f}\n'.format(values[0],values[1],values[2], float(values[7])))
    except ValueError :
        print('mpg value was invalid')
file.close()
out.close()
