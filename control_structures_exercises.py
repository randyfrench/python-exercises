# Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not
#day_of_the_week = input("What is today?")
#if day_of_the_week.lower() == "monday":
        #print("Is is Monday")
#else:
        #print("It is not Monday")

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = input("What is today?")
if day_of_the_week.lower() == 'monday' or 'tuesday' or 'wednesday' or 'thursday'or 'friday':
        print("Is is a weekday!")
elif day_of_the_week.lower() == 'saturday' or 'sunday':
        print("It is a weekend!")
else:
    print("I have to get this Python down!")
# c. create variables and make up values for
hrs_worked_in_one_week = 40   #the number of hours worked in one week
hourly_rate = 40        #the hourly rate
total = hrs_worked_in_one_week * hourly_rate
print(f"Total week's paycheck is ${total}")       #how much the week's paycheck will be

    #write the python code that calculates the weekly paycheck. You get paid time and a half if you 
    # work more than 40 hours
hrs_worked_in_one_week = 40  #the number of hours worked in one week
hourly_rate = 40  #the hourly rate
more_than_40hrs = 5
time_and_half = 60  # the time and a half rate     
total = hrs_worked_in_one_week * hourly_rate
print(f"Total week's paycheck is ${total}")
