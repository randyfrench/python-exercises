# Conditional Basics
# a. prompt the user for a day of the week, print out whether the day is Monday or not

day = input("What day of the week is it?   ")
if day.lower() == "monday":
    
    print("Today is monday")
    
else:
    
    print("Today is not monday")


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
print("What day of the week is it?")
day = input()

if day.lower() in ("monday", "tuseday", "wednesday", "thursday", "friday"):
    
    print()
    print("Today is a weekday!")
    
elif day.lower() in ("saturday", "sunday"):
    
    
    print()
    print("Today is a weekend!")
    
else:
    
    print()
    print(f"{day} is not a day of the week!")

# c. create variables and make up values for
# 
#   the number of hours worked in one week
#    the hourly rate
#    how much the week's paycheck will be

# write the python code that calculates the weekly paycheck. You get paid time and a half 
# if you work more than 40 hours

hours_this_week = 50
hourly_rate = 20

if hours_this_week <= 40:
    
    pay = hours_this_week * hourly_rate 

if hours_this_week > 40:
    
    overtime = (hours_this_week - 40) * (hourly_rate * 1.5)
    
    pay = (40 * hourly_rate) + overtime

print(f"Total Wages: {pay}")


# 2 Loop Basics

    #While
# i = 5       #Create an integer variable i with a value of 5.
# while i <= 15:  # Create a while loop that runs so long as i is less than or equal to 15.
        # print(i)
        # Each loop iteration, output the current value of i, then increment i by one.
i = 0
i = 5
while i <= 15:
    print(i)
    i += 1
    #Your output should look like this:

#5,6,7,8,9,10,11,12,13,14,15

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with 
# a new line.
x = 0
while x <= 100:
    print(x)
    x += 2

# Alter your loop to count backwards by 5's from 100 to -10.
x = 100
while x > -15:
    print(x)
    x -= 5



# Create a while loop that starts at 2, and displays the number squared on each line while the number is
 # less than 1,000,000. Output should equal:
x = 2
while x < 10000000:
    print(x)
    x = x **2

# Write a loop that uses print to create the output shown below.
# 100 down to 5
x = 100
while x > 0:
    print(x)         
    x -= 5

#For Loops

    #Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

    #For example, if the user enters 7, your program should output:
     
number = int(input("Enter your number: "))
for num in range(1, 11):
    print("{0} x {1} = {2}".format(number, num, (number * num)))
     

#7 x 1 = 7

# 2b ii. Create a for loop that uses print to create the output shown below.
for r in range(1,10):
    print(str(r) * r)

#C.break and continue

    #Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue 
    # prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to 
    # determine this). Use a loop and the continue statement to output all the odd numbers between 1 
    # and 50, except for the number the user entered.
 number = int(input("Enter an odd number between 1 and 50: "))   

    #Your output should look like this:

# Number to skip is: 27

# Here is an odd number: 1
# Here is an odd number: 3
# Here is an odd number: 5
# Here is an odd number: 7
# Here is an odd number: 9
# Here is an odd number: 11
# Here is an odd number: 13
# Here is an odd number: 15
# Here is an odd number: 17
# Here is an odd number: 19
# Here is an odd number: 21
# Here is an odd number: 23
# Here is an odd number: 25
# Yikes! Skipping number: 27
# Here is an odd number: 29
# Here is an odd number: 31
# Here is an odd number: 33
# Here is an odd number: 35
# Here is an odd number: 37
# Here is an odd number: 39
# Here is an odd number: 41
# Here is an odd number: 43
# Here is an odd number: 45
# Here is an odd number: 47
# Here is an odd number: 49



#2 d.The input function can be used to prompt for input and use that input in your python code. Prompt 
#  user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first 
# make sure that the value the user entered is a valid number, also note that the input function 
# returns a string, so you'll need to convert this to a numeric type.)

#2 e. Write a program that prompts the user for a positive integer. Next write a loop that prints out 
# the numbers from the number the user entered down to 1.



#3. Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

    # Write a program that prints the numbers from 1 to 100.
    # For multiples of three print "Fizz" instead of the number
    # For the multiples of five print "Buzz".
    # For numbers which are multiples of both three and five print "FizzBuzz".



#4. Display a table of powers.

#     Prompt the user to enter an integer.
#     Display a table of squares and cubes from 1 to the value entered.
#     Ask if the user wants to continue.
#     Assume that the user will enter valid data.
#     Only continue if the user agrees to.

# Example Output

# What number would you like to go up to? 5

# Here is your table!

# number | squared | cubed
# ------ | ------- | -----
# 1      | 1       | 1
# 2      | 4       | 8
# 3      | 9       | 27
# 4      | 16      | 64
# 5      | 25      | 125

# Bonus: Research python's format string specifiers to align the table

