# 1. Define a function named is_two. It should accept one input and return True if the passed 
    # input is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    else:
        return False
is_two(2)

    # 2. Define a function named is_vowel. It should return True if the passed string is a vowel, 
    # False otherwise.ef is_vowel(string):
def is_vowel(string):   
    vowles = "AEIOUaeiou"
    for x in string:
        if x in string[0] in vowles:
            return True
        else:
            return False
    return vowels
is_vowel('U') 

    # 3. Define a function named is_consonant. It should return True if the passed string is a 
    # consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(string):
    consonant = "bcdfghjklmnpqrstvwxyz"
    for x in string:
        if x in string[0] in consonant:
            return True
        else:
            return False
    return consonant
is_consonant("B")    

    # 4. Define a function that accepts a string that is a word. The function should capitalize the 
    # first letter of the word if the word starts with a consonant.
# def is_consonant(string):
#     consonant = "bcdfghjklmnpqrstvwxyz"
#     for x in string:
#         if x in string[0] in consonant.capitalize():
#     return consonant
# is_consonant("potlicker")

    # 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 
    # and 1) and the bill total, and return the amount to tip.
def calculate_tip(bill, tip_percent):
    
    return bill * tip_percent

bill = 100
tip_percent = .20

calculate_tip(bill, tip_percent)

    # 6. Define a function named apply_discount. It should accept a original price, and a discount 
    # percentage, and return the price after the discount is applied.
def apply_discount(price, discount_percent):
    
    return price - (price * discount_percent / 100)

price = 500
discount_percent = 50

apply_discount(price, discount_percent)
    


    # 7. Define a function named handle_commas. It should accept a string that is a number that 
    # contains commas in it as input, and return a number as output.
def handle_commas(string):
    number = ""
    for char in string:
        if char not in ",":
            number += char
    return float(number)

string = "2,0,1,25.5,42,0,0,10"
handle_commas(string)

    # 8. Define a function named get_letter_grade. It should accept a number and return the letter 
    # grade associated with that number (A-F).
#def get_letter_grade(x):


  # 9. Define a function named remove_vowels that accepts a string and returns a string with all 
    # the vowels removed.
#def remove_vowels(x):

    # 10. Define a function named normalize_name. It should accept a string and return a valid python 
    # identifier, that is:
    #     anything that is not a valid python identifier should be removed
    #     leading and trailing whitespace should be removed
    #     everything should be lowercase
    #     spaces should be replaced with underscores
    #     for example:
    #         Name will become name
    #         First Name will become first_name
    #         % Completed will become completed
#def normalize_name(x):

    # 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list 
    # that is the cumulative sum of the numbers in the list.
    #     cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #     cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
#def cumulative_sum(x)
  