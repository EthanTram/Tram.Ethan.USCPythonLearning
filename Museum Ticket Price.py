# Set days of the week
DaysOfTheWeek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# Print Welcome Message
print ("Welcome to the Museum!")
age = input("Please enter your age: ")
day = input("What day(s) of the week are you visiting for? : ")
coupon_code = input("Enter a coupon a code if you have one: ")

# Make sure age is a valid number and find their visiting days
if age.isalpha() or int(age) <= 0:
    print ("Age is not vaild")

elif day not in DaysOfTheWeek:
    print ("Invalid day of the week")

else:
    # Ticket day and age correlation
    if 0 <= int(age) <= 5:
        price = 0
    elif 6 <= int(age) <= 17:
        if day == 'monday':
            price = 5
        elif day in ['tuesday', 'wednesday', 'thursday']:
            price = 10
        else:
            price = 15
    elif 18 <= int(age) <= 64:
        if day in ['monday', 'tuesday', 'wednesday', 'thursday']:
            price = 15
        else:
            price = 25
    elif int(age) >= 65:
        if day in ['monday', 'tuesday', 'wednesday', 'thursday']:
            price = 10
        else:
            price = 15

    # Apply coupon codes
    if coupon_code == 'HALFOFF':
        price /= 2
    elif coupon_code == 'MINUS5':
        price -= 5

    # Ensure the price is not negative
    price = max(price, 0)

    # Output the ticket price
    print("Ticket price: ${:.2f}" .format(price))