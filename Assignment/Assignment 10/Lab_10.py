##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 10
##
##########################################

'''
1. ask user to read textfile 
2. read all words and ouput count of words that are used most (length 3 or longer)
    a. remove punction from bgeinning and ending of word, 
    b. previous sentance words should be counted once, 
    c. not words followed by period

    output top 10 words that are used most
    most frequenctly used words at the top
    excluse words 3 characters or less

    output number words that appear only once 
        output how may unique words there are 
    
    recover gracefully from user providing an invalid file
'''

frequency = {}

def get_file_name():
    print()
    game = True
    while game == True: 
      try:
          file_name = input("Enter the name of the file to open ")
          file = open(file_name, 'r')
          file.close
          game = False
      except FileNotFoundError:
              print("Could not open file", file_name)
              print("Please try again")
              print()
              game = True
    return file_name

def getting_nums(file_name):
  with open(file_name, "r") as f:
    for line in f: 
      line = line.lower()
      line = line.replace(',',' ')
      line = line.replace('.',' ')
      line = line.replace('!',' ')
      line = line.replace('-',' ')
      line = line.replace('\n', ' ')
      line = line.split(" ")
      for word in line: 
        frequency[word] = frequency.get(word, 0) + 1
  frequency.pop("")

def deletes():
  #cutting it short
  new_dict = {key:frequency[key] for key in frequency if len(key) >= 4}
  new_freq = dict(sorted(new_dict.items(), key=lambda key:key[1], reverse=True))
  #editing
  return new_freq

def print_menu():
  print("Most frequently used words")
  num = "#"
  w = "Word"
  fre = "Freq."
  line = "====================================="
  print("{:<10} {:>12} {:>12}".format(num, w, fre))
  print(line)

def output(new_freq):
  i = 1
  game = True
  while game == True: 
    for key in new_freq:
      print("{:<10} {:>12} {:>12}".format(i, key, new_freq[key]))
      #add to i 
      i += 1
      if i > 10: 
        game = False
        break

def once(new_freq):
  i = 0
  for key in new_freq:
    if new_freq[key] == 1:
      i += 1
  return i 

def unique(new_freq):
  i = 0
  for key in new_freq:
    i += 1 
  return i

if __name__ == "__main__":
    #getting correct file
    file = get_file_name()

    #getting list order into FREQUENCY(unordered)
    getting_nums(file)
    '''print(frequency)''' #(dictionary unsorted)

    print()
    #deleting 3 or less
    new_list = deletes()
    '''print(new_list)''' #(sorted dictionary)

    #meny
    print_menu()
    #output
    output(new_list)
    
    #words occur only once
    num1 = once(new_list)

    print("There are", num1, "words that occur only once")

    #bottom
    num2 = unique(new_list)
    print("There are", num2, "unique words in the document")

