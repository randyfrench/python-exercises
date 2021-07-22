# You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear 
# (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to 
# like it). If price for a movie per day is 3 dollars, how much will you have to pay?

price_per_day = 3
little_mermaid_days = 3
brother_bear_days = 5
hercules_days = 1
days = little_mermaid_days + brother_bear_days + hercules_days
total = days * price_per_day
print(f"Total rental price is ${total}")

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, 
# and Facebook 350. How much will you receive in payment for this week? You worked 10 
# hours for Facebook, 6 hours for Google and 4 hours for Amazon.


google_rate = 400
amazon_rate = 380
facebook_rate = 350
google_hours = 6
facebook_hours = 10
amazon_hours = 4
amazon_pay = amazon_rate * amazon_hours
google_pay = google_hours * google_rate
facebook_pay = facebook_hours * facebook_rate
total = amazon_pay + google_pay + facebook_pay
print(f"Total compensation is ${total}")

# A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.

class_has_room = True
schedule_works_for_student = False
student_can_enroll = class_has_room and schedule_works_for_student
print(f"The class has room is", class_has_room)
print(f"The class fits the student's schedule", schedule_works_for_student)
print(f"Can the student can enroll?", student_can_enroll)

# A product offer can be applied only if people buys more than 2 items, and the offer 
# has not expired. Premium members do not need to buy a specific amount of products.

s_premium_member = True
more_than_2_items = False
offer_still_good = True
offer_can_be_applied = offer_still_good and (more_than_2_items or is_premium_member)

# Use the following code to follow the instructions below:

# username = 'codeup'
# password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:

    #the password must be at least 5 characters
password_is_long_enough = len(password) >= 5

    #the username must be no more than 20 characters
username_is_short_enough = len(username) <= 20

    #the password must not be the same as the username
username_and_password_are_different = username != password

    #bonus neither the username or password can start or end with whitespace
username_has_spaces = username != username.strip()
password_has_spaces = password != password.strip()

username_is_good = username_is_short_enough and username_and_password_are_different and not username_has_spaces
password_is_good = password_is_long_enough and username_and_password_are_different and not password_has_spaces

credentials_are_good = username_is_good and password_is_good

print(username, password)
print("Password is long enough?", password_is_long_enough)
print("Username is short enough?", username_is_short_enough)
print("Username and password are different", username_and_password_are_different)
print("Username has spaces", username_has_spaces)
print("Password has spaces", password_has_spaces)
print("Username is good?", username_is_good)
print("Password is good?", password_is_good)
print("------")
print("Credentials are good?", credentials_are_good)


