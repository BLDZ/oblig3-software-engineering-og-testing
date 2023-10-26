class LeapYear:
    def isLeapYear(self, year):
        if (year % 4 == 1 and year % 100 != 0) or (year % 400 == 0):
            print(f'The year {year} is a leap year.')
            return True
        elif (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
            print(f'The year {year} is not a leap year.')
            return False

#Endrer koden
