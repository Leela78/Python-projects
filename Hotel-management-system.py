# Hotel Bill Management System - Beginner Version

print("----- Welcome to Hotel Bill Management System -----\n")

# Rooms and their costs
print("Available Rooms:")
print("1. Single - 1000")
print("2. Double - 2000")
print("3. Suite - 3500")

room_choice = input("Enter room type (1/2/3): ")

if room_choice == "1":
    room_cost = 1000
    room_name = "Single"
elif room_choice == "2":
    room_cost = 2000
    room_name = "Double"
elif room_choice == "3":
    room_cost = 3500
    room_name = "Suite"
else:
    room_cost = 0
    room_name = "Invalid"
    print("Invalid room choice! Cost set to 0.")

# Food selection
print("\nAvailable Food:")
print("1. Breakfast - 150")
print("2. Lunch - 300")
print("3. Dinner - 400")

food_choice = input("Enter food choice (1/2/3): ")

if food_choice == "1":
    food_cost = 150
    food_name = "Breakfast"
elif food_choice == "2":
    food_cost = 300
    food_name = "Lunch"
elif food_choice == "3":
    food_cost = 400
    food_name = "Dinner"
else:
    food_cost = 0
    food_name = "Invalid"
    print("Invalid food choice! Cost set to 0.")

# Extra services
print("\nAvailable Extra Services:")
print("1. Laundry - 200")
print("2. WiFi - 100")
print("3. None - 0")

service_choice = input("Enter service (1/2/3): ")

if service_choice == "1":
    service_cost = 200
    service_name = "Laundry"
elif service_choice == "2":
    service_cost = 100
    service_name = "WiFi"
elif service_choice == "3":
    service_cost = 0
    service_name = "None"
else:
    service_cost = 0
    service_name = "Invalid"
    print("Invalid service choice! Cost set to 0.")

# Calculate total
total = room_cost + food_cost + service_cost
tax = total * 10 / 100  # 10% tax
grand_total = total + tax

# Print bill
print("\n----- Final Bill -----")
print("Room ({}): {}".format(room_name, room_cost))
print("Food ({}): {}".format(food_name, food_cost))
if service_name != "None":
    print("Service ({}): {}".format(service_name, service_cost))
print("Subtotal:", total)
print("Tax (10%):", tax)
print("Grand Total:", grand_total)
print("------------------------")
print("Thank you! Visit again 😊")

