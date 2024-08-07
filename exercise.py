# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    x = input("Enter a letter from a-z or A-Z: ").lower()
    print(f'the user entered letter {x}')

    if x in ["a", "e", "i", "o", "u"]:
        print(f"The letter {x} is a vowel")
    elif x not in ["a", "e", "i", "o", "u"]:
        print(f"The letter {x} is a consonent")
    else:
        print("non available entry")
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.


def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input("Please enter your age: "))
    voting_age = True if age >= 18 else False
    if voting_age:
        print(f"The personcan vote")
    else:
        print(f"the person can't vote, is too young")

check_voting_eligibility()


def check_voting_eligibility():
    # Your control flow logic goes here
    age = int(input("Please enter your age: "))
    voting_age = "You can vote" if age >= 18 else "You can't vote"
    print(voting_age)

check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = int(input("Input a dog's age: "))

    if dog_age == 1:
        print("The dog's age in dog years is 10.")
    elif dog_age == 2:
        print("The dog's age in dog years is 20.")
    elif dog_age > 2:
        print(f"The dog's age in dog years is {20 + (dog_age -2) *7}")
    else:
        print("NA")
# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold = input('It is cold, enter "yes" or "no"')
    raining = input('Is it raining, enter "yes" or "no"')

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")

# Call the function
weather_advice()


# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    # Your control flow logic goes here
    month = input( "Enter the month of the year (Jan - Dec):")
    day = int(input("Enter the day of the month:"))


    if (month == "Dec" and 21 <= day <= 31) or (month == "Jan") or (month == "Feb") or (month == "Mar" and 1 <= day <= 19):
        print(f"{month} + {day} is in Winter")

    elif (month == "Mar" and 20 <= day <=31) or (month == "Apr") or (month == "May") or (month == "Jun" and  1<= day <= 20):
        print(f"{month} + {day} is in Spring")

    elif (month == "Jun" and 21 <= day <= 30) or (month == "Jul") or (month == "Aug") or (month == "Sep" and 1 <= day <= 21):
        print(f"{month} {day} is in Summer")

    elif (month == "Sep" and 22 <= day <= 30) or (month == "Oct") or (month == "Nov") or (month == "Dec" and 1 <= day <= 20):
        print(f"{month} {day} is in Fall")
    else:
        print("This is not a valid entry")

determine_season()


#Level Up

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Congratulations, you guessed correctly!"if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.
import random
def guess_number():

    for guess in range(5):
        number = random.randint(1, 100)
        number_guessed = int(input("Guess a number between 1 to 100: "))
        if number > number_guessed:
            print("Guess is too low")
        elif number < number_guessed:
            print("Guess it too high")
        elif number == number_guessed:
            print("Congratulations, you guessed correctly!")
            break
    else:
        print("nope, you did not guessed correctly!")

# Call the function
guess_number()
