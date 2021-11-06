##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 9
##
##########################################

import csv

#Month to Number function
def month_from_number(user_num):
  game = True
  while game == True:
    if user_num >= 1 and user_num <= 12:
      if user_num == 1:
        month = "January"
      elif user_num == 2:
        month = "Febuary"
      elif user_num == 3:
        month = "March"
      elif user_num == 4:
        month = "April"
      elif user_num == 5: 
        month = "May"
      elif user_num == 6:
        month = "June"
      elif user_num == 7:
        month = "July"
      elif user_num == 8:
        month = "August"
      elif user_num == 9:
        month = "September"
      elif user_num == 10:
        month = "October"
      elif user_num == 11:
        month = "November"
      elif user_num == 12:
        month = "December"
      game = False
      break
    else:
      print("Month must be 1-12")
      user_num = int(input(''))
  #returns the month string
  return month

#Read in file function:
def read_in_file():
  file_name = input("Enter file name ")
  list_of_list = []
  with open(file_name, 'r') as csv_file:
    for line in csv_file:
      list_of_list.append(line.strip().split(','))
  return list_of_list
  '''list_of_list[1][1], list_of_list[2][7], list_of_list[3][13]'''

def create_reported_date_dict(lst):
  dictionary = {}
  try:
    for i in range(1, len(lst)):
      for j in range(len(lst[i])):
        if "/" in lst[i][j]:
          dictionary[lst[i][j]] = dictionary.get(lst[i][j], 0) + 1 
    return dictionary
  except KeyError: 
    print("KeyError then")


def create_reported_month_dict(lst):
  number_date = []
  for i in range(1, len(lst)):
    number_date = []
    number_date.append(lst[i][1])
    split_date = number_date[0]
    month = month_from_number(split_date)
  return month

def create_offense_dict(lst):
  try: 
    dictionary = {}
    for elem in lst[1:]:
      offense = elem[7]
      if offense in dictionary: 
        dictionary[offense] += 1
      else: 
        dictionary[offense] = 1
    return dictionary
  except KeyError: 
    print("KeyError")

def create_offense_by_zip(lst):
    try: 
      dictionary = {}
      dict2 = {}
      for elem in lst[1:]:
        offense = elem[7]
        dictionary[offense] = {}
        for elem in lst[1:]:
          zipcode = elem[13]
          if zipcode in dict2:
            dict2[zipcode] += 1
          else:
            dict2[zipcode] = 1
      result = dictionary[offense] = dict2
      return result
    except KeyError: 
      print("KeyError")

if __name__ == "__main__":

  #Test month_from_number function:
  print(month_from_number())
  test = read_in_file()
  test1 = create_reported_date_dict(test)
  test2 = create_offense_dict(test)
  test3 = create_offense_by_zip(test)
  print(test)
  print(test1)
  print(test2)
  print(test3)