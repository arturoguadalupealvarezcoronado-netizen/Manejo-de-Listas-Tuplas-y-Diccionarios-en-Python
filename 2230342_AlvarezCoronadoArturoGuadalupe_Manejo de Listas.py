# ================================================
# Collections Assignment: Lists, Tuples, Dictionaries
# Student-style solution
# ================================================

# ------------------------------------------------
# Problem 1: Shopping list basics (list operations)
# Description:
# This program works with a shopping list using a Python list.
# It creates an initial list, adds a new item, counts elements,
# and checks if a product exists in the list.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - Items list
# - Total items
# - Found item (True/False)
#
# Validations:
# - Input strings must not be empty
#
# Test cases:
# 1) Normal: "apple, banana" / "orange" / "banana"
# 2) Edge: "apple" / "apple" / "apple"
# 3) Error: "" / "" / ""
# ------------------------------------------------

initial_items_text = input("Enter initial items: ").strip()

if initial_items_text == "":
    print("Error: invalid input")
else:
    items_list = [item.strip().lower() for item in initial_items_text.split(",") if item.strip() != ""]

    new_item = input("Enter new item: ").strip().lower()
    search_item = input("Enter item to search: ").strip().lower()

    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = search_item in items_list

        print("Items list:", items_list)
        print("Total items:", len(items_list))
        print("Found item:", is_in_list)


# ------------------------------------------------
# Problem 2: Points and distances with tuples
# Description:
# Uses tuples to represent two points in a 2D plane,
# calculates the distance between them and their midpoint.
# ------------------------------------------------

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 2))
    print("Midpoint:", midpoint)
except:
    print("Error: invalid input")


# ------------------------------------------------
# Problem 3: Product catalog with dictionary
# Description:
# Manages a small product catalog and calculates total price.
# ------------------------------------------------

product_prices = {
    "apple": 10.0,
    "banana": 8.5,
    "orange": 12.0
}

product_name = input("Enter product name: ").strip().lower()

try:
    quantity = int(input("Enter quantity: "))

    if product_name == "" or quantity <= 0:
        print("Error: invalid input")
    elif product_name not in product_prices:
        print("Error: product not found")
    else:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
except:
    print("Error: invalid input")


# ------------------------------------------------
# Problem 4: Student grades with dict and list
# Description:
# Calculates the average grade of a student and checks if passed.
# ------------------------------------------------

grades = {
    "alice": [85.0, 90.0, 78.0],
    "bob": [60.0, 70.0, 65.0],
    "carol": [95.0, 88.0, 92.0]
}

student_name = input("Enter student name: ").strip().lower()

if student_name == "":
    print("Error: invalid input")
elif student_name not in grades:
    print("Error: student not found")
elif len(grades[student_name]) == 0:
    print("Error: invalid input")
else:
    grades_list = grades[student_name]
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0

    print("Grades:", grades_list)
    print("Average:", round(average, 2))
    print("Passed:", is_passed)


# ------------------------------------------------
# Problem 5: Word frequency counter
# Description:
# Counts how many times each word appears in a sentence.
# ------------------------------------------------

sentence = input("Enter a sentence: ").strip().lower()

if sentence == "":
    print("Error: invalid input")
else:
    for symbol in ".,!?;:":
        sentence = sentence.replace(symbol, "")

    words_list = sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        most_common_word = max(freq_dict, key=freq_dict.get)

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


# ------------------------------------------------
# Problem 6: Simple address book (dictionary CRUD)
# Description:
# Implements a basic address book with add, search and delete.
# ------------------------------------------------

contacts = {
    "Alice": "1234567890",
    "Bob": "5551234567"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
else:
    name = input("Enter contact name: ").strip().title()

    if name == "":
        print("Error: invalid input")
    elif action_text == "ADD":
        phone = input("Enter phone: ").strip()
        if phone == "":
            print("Error: invalid input")
        else:
            contacts[name] = phone
            print("Contact saved:", name, phone)

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
