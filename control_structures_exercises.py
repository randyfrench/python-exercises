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
more_than_40hrs = 5  # above 40 hours worked
time_and_half = 60  # the time and a half rate     
total = hrs_worked_in_one_week * hourly_rate + more_than_40hrs * time_and_half
print(f"Total week's paycheck is ${total}")

#2Loop Basics

    #While
#i = 5       #Create an integer variable i with a value of 5.
#while i <= 15:  # Create a while loop that runs so long as i is less than or equal to 15.
        #print(i)
        #Each loop iteration, output the current value of i, then increment i by one.
i = 0
i = 5
while i <= 15:
        print(i)
        i = i + 1
    #Your output should look like this:

#5,6,7,8,9,10,11,12,13,14,15

#Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with 
#a new line.
x = 0
x = 2
while x <= 100:
        print(x)
        x = x + 2

#Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x > -15:
        print(x)
        x = x - 5



#Create a while loop that starts at 2, and displays the number squared on each line while the number is
 #less than 1,000,000. Output should equal:
