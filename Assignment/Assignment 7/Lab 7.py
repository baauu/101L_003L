##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 8
##
##########################################

#Min MPG
def min_MPG():
    try:
        user_input = float(input("Enter the minimum mpg ==> "))    
        while user_input < 0 and user_input > 100:
            if user_input < 0: 
                print("Fuel economy given must be greater than 0")
            elif user_input > 100:
                print("Fuel economy must be less than 100")
            else:
                user_input = float(input("Enter the minimum mpg ==> ")) 
        return user_input
    except ValueError:
        print("You must enter a number for the fuel economy")
        user_input = float(input("Enter the minimum mpg ==> "))    
        while user_input < 0 and user_input > 100:
            if user_input < 0: 
                print("Fuel economy given must be greater than 0")
            elif user_input > 100:
                print("Fuel economy must be less than 100")
            else:
                user_input = float(input("Enter the minimum mpg ==> ")) 
        return user_input            

def accessing_file():
    try:
        file_name = input("Enter the name of the input vehicle file ==> ")
        if file_name == "vehicle.txt" or file_name == "vehicle2.txt":
          return file_name
        else: 
          try_again = True
          while try_again == True:
              print("Could not open file invalidfile.txt")
              file_name = input("Enter the name of the input vehicle file ==> ")
              if file_name == "vehicle.txt" or file_name == "vehicles2.txt":
                return file_name
    except IOError: 
        print("There is an IO Error")
        file_name = input("Enter the name of the input vehicle file ==> ")
        while file_name != "vehicles2.txt" or file_name != "vehicles.txt":
            print("Could not open file invalidfile.txt")
            file_name = input("Enter the name of the input vehicle file ==> ")
        return file_name

def finding_type(MPG, file_name, output):
      with open(file_name, 'r') as f, open(output, 'w') as t:
          next(f)
          for line in f:
              new_file = line.split("\t")
              mpg_file_num = new_file[7]
              try:
                mpg_num = round(float(mpg_file_num), 3)
                if mpg_num >= MPG:
                    t.write("{:<5} {:<15} {:<25} {:>6}\n".format(new_file[0],new_file[1], new_file[2], mpg_num))
                else:
                    continue
              except ValueError:
                print("Could not convert value invalid for {} {} {}\n".format(new_file[0],new_file[1], new_file[2]))
                continue
                


def getting_output():
    try:
        file_name = input("Enter the name of the file to output to ==> ")
        if file_name == "output.txt":
          return file_name
          
    except IOError: 
        print("There is an IO Error")
        try_again = True
        while try_again == True:
            file_name = input("Enter the name of the file to output to ==> ")
            if file_name == "output.txt":
                try_again = False
                break
        return file_name


if __name__ == "__main__":
    user_input = min_MPG()
    print()
    file = accessing_file()
    output_file = getting_output()
    finding_type(user_input, file, output_file)


