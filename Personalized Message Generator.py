#welcome message
print ("Welcome!")

# Prompt the user
firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")
age = int(input("Enter Age: "))
integer = int(input("Enter integer: "))
favoriteColor = input("Favorite Color: ")

# Calculate future age and name length
futureAge = age + integer
nameLength = len(firstName + lastName)

# Message
print ("Hello, " + firstName + " " + lastName + "! Your name is " + str(nameLength) + " characters long.")
print ("In " + str(integer) + " years, you will be " + str(futureAge) + " years old. Your favorite color is " + favoriteColor.upper() + "!")