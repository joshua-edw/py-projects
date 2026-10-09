# This is a chatbot that interacts with the user to gather the user's name, age, birth date, and calculates their birth year, 
# day of the week they were born, and zodiac sign.

from datetime import date

# Name, age
print("Hello, I am a chatbot. In order to proceed, please provide your name.")
name = str(input("Your name is: "))
print(f"Nice to meet you, {name}! Now, let's learn more about you. What is your age?")
age = int(input("Your age is: "))
if age >= 18:
    print(f"Great! You are {age} years old, which means you are an adult.")
elif age <= 0:
    print("It seems like you entered an invalid age. Please enter a valid age.")
    age = int(input("Your age is: "))
elif age < 18:
    print(f"You are {age} years old, which means you are a minor.")
else:
    print("It seems like you entered an invalid age. Please enter a valid age.")
    age = int(input("Your age is: "))

# Birth year, day of the week
print(f"Thank you for providing your age, {name}. I will now calculate your birth year using your age, {age}, based on the current year.")
current_year = date.today().year
birth_year = current_year - age
print(f"Based on your age, you were born in {birth_year}.")
print(f"Now that I have your birth year, I can also calculate the day of the week that you were born. Please provide your birth month and day in the format MM-DD.")
birth_month = int(input("Your birth month is: "))
if birth_month < 1 or birth_month > 12:
    print("It seems like you entered an invalid month. Please enter a valid month.")
    birth_month = int(input("Your birth month is: "))
birth_day = int(input("Your birth day is: "))
if birth_day < 1 or birth_day > 31:
    print("It seems like you entered an invalid day. Please enter a valid day.")
    birth_day = int(input("Your birth day is: "))
birthday = date(birth_year, birth_month, birth_day)
day_of_week = birthday.strftime("%A")
print(f"You were born on a {day_of_week}; that's interesting!")

# Zodiac sign
print(f"We can also use this information to calculate your zodiac sign.")
if (birth_month == 3 and birth_day >= 21) or (birth_month == 4 and birth_day <= 19):
    zodiac_sign = "Aries"
elif (birth_month == 4 and birth_day >=
    20) or (birth_month == 5 and birth_day <= 20):
     zodiac_sign = "Taurus"
elif (birth_month == 5 and birth_day >= 21) or (birth_month == 6 and birth_day <= 20):
     zodiac_sign = "Gemini"
elif (birth_month == 6 and birth_day >= 21) or (birth_month == 7 and birth_day <= 22):
      zodiac_sign = "Cancer"
elif (birth_month == 7 and birth_day >= 23) or (birth_month == 8 and birth_day <= 22):
     zodiac_sign = "Leo"
elif (birth_month == 8 and birth_day >= 23) or (birth_month == 9 and birth_day <= 22):
     zodiac_sign = "Virgo"
elif (birth_month == 9 and birth_day >= 23) or (birth_month == 10 and birth_day <= 22):
     zodiac_sign = "Libra"
elif (birth_month == 10 and birth_day >= 23) or (birth_month == 11 and birth_day <= 21):
      zodiac_sign = "Scorpio"
elif (birth_month == 11 and birth_day >= 22) or (birth_month == 12 and birth_day <= 21):
     zodiac_sign = "Sagittarius"
elif (birth_month == 12 and birth_day >= 22) or (birth_month == 1 and birth_day <= 19):
     zodiac_sign = "Capricorn"
elif (birth_month == 1 and birth_day >= 20) or (birth_month == 2 and birth_day <= 18):
     zodiac_sign = "Aquarius"
else:
      zodiac_sign = "Pisces"
print(f"Your zodiac sign is {zodiac_sign}.")   