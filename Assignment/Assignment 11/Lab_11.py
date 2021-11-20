##########################################
##
## Jessi Bautista Espino
## jbr75@umsystem.edu 
## CS 101 Lab
## Program 11
##
##########################################
import time
class clock:
    def __init__(self, hour, minu, sec, clock_type = 0):
        self.hr = hour
        self.min = minu
        self.sec = sec
        self.clock_type = 1
        
    def tick(self):
        self.sec += 1
        if self.sec > 59:
            self.min += 1
            self.sec = 0
        if self.min > 59:
            self.hr += 1
            self.min = 0
        if self.hr > 24:
            self.hr = 0 

    def __str__(self):
        if self.clock_type == 0:
            return ("{:02d}:{:02d}:{:02d}".format(self.hr, self.min, self.sec))
        elif self.clock_type == 1:
            time_letters = "AM"
            if self.hr > 12:
                time_letters = "PM"
                if self.hr < 0:
                    pass
                else:
                    self.hr = self.hr - 12
            return ("{:02d}:{:02d}:{:02d} {}".format(self.hr, self.min, self.sec, time_letters))
    


if __name__ == "__main__":
    hour = int(input("What is the current hour ==>  "))
    minute = int(input("What is the current minute ==>  "))
    second = int(input("What is the current second ==>  "))
    '''c_type = int(input("24hr clock = 0, AM/PM = 1: "))'''

    output = clock(hour, minute, second) #c_type variable not included just here for checking it worked
    '''print(output)'''

    while True:
        print(output)
        output.tick()
        '''print(output)'''
        time.sleep(1) 


    


