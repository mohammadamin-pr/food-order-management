def delivery_fee(distance):
    if distance <= 5:
        return 5
    elif distance <= 10:
        return 8
    else:
        return 12


def discount_price(price, code):
    if code == "OFF10":
        return price * 10 / 100
    elif code == "OFF20":
        return price * 20 / 100
    else:
        return 0


menu = {
    "Pizza": 12,
    "Burger": 9,
    "Fried Chicken": 11,
    "Pasta": 10,
    "Taco": 7,
    "Sushi": 15
}

print("Food Order Management System")

name = input("Enter your name: ")

orders = []
total = 0

while True:
    print("Food Menu")

    print("1. Pizza - $12")
    print("2. Burger - $9")
    print("3. Fried Chicken - $11")
    print("4. Pasta - $10")
    print("5. Taco - $7")
    print("6. Sushi - $15")

    choice = input("Choose a food: ")

    if choice == "1":
        food = "Pizza"
        price = menu["Pizza"]
    elif choice == "2":
        food = "Burger"
        price = menu["Burger"]
    elif choice == "3":
        food = "Fried Chicken"
        price = menu["Fried Chicken"]
    elif choice == "4":
        food = "Pasta"
        price = menu["Pasta"]
    elif choice == "5":
        food = "Taco"
        price = menu["Taco"]
    elif choice == "6":
        food = "Sushi"
        price = menu["Sushi"]
    else:
        print("Invalid choice")
        continue

    print("You selected:", food)
    print("Price:", price, "dollars")

    confirm = input("Is this okay? (yes/no): ")

    if confirm == "yes":
        orders.append(food)
        total = total + price

        another = input("Do you want another food? (yes/no): ")

        if another == "no":
            break

    elif confirm == "no":
        print("Choose another food")
        continue

    else:
        print("Please enter yes or no")


print("Order Summary")
print("Customer:", name)

print("Foods:")
for food in orders:
    print("-", food)

quantity = int(input("Enter quantity: "))

total = total * quantity

vip = input("Are you a VIP customer? (yes/no): ")

distance = float(input("Enter delivery distance: "))

delivery = delivery_fee(distance)

code = input("Enter discount code (OFF10/OFF20 or none): ")

discount = discount_price(total, code)

final_price = total + delivery - discount

print("Food price:", total)
print("VIP:", vip)
print("Delivery fee:", delivery)
print("Discount:", discount)
print("Final price:", final_price)