import os
import csv
import json


# ---------------- CSV ----------------

def csv_menu():
    file_name = input("Enter File Name : ")
    check = file_name + ".csv"

    # Create a new CSV or open an existing one
    if os.path.exists(check):
        print("File already exists.")
        with open(check, "r", newline="") as f:
            reader = csv.reader(f)
            try:
                categories = next(reader)
            except StopIteration:
                categories = []

        if not categories:
            print("CSV file is empty.")
            return

        print("Categories found:", categories)

    else:
        while True:
            print("\nHow many categories do you want? (1-5)")
            list_no = input("Enter number : ")

            if list_no.isdigit() and 1 <= int(list_no) <= 5:
                number = int(list_no)
                break

            print("Invalid input. Enter a number from 1-5.")

        categories = []
        for i in range(number):
            categories.append(input(f"Enter category {i + 1} : "))

        with open(check, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(categories)

        print("Your CSV File Created Successfully!")

    while True:
        print("\n--- CSV Menu ---")
        print("1. Add Input in File")
        print("2. View File")
        print("3. Back To Menu")

        choice = input("Choose : ")

        if choice == "1":
            row = []

            # One value for each category = one complete CSV row
            for category in categories:
                row.append(input(f"Enter {category} : "))

            with open(check, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(row)

            print("Information Added Successfully!")

        elif choice == "2":
            with open(check, "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    print(row)

        elif choice == "3":
            break

        else:
            print("Invalid Input.")


# ---------------- JSON ----------------

def json_menu():
    file_name = input("Enter File Name : ")
    check = file_name + ".json"

    # If the file already exists, do not enter the JSON creation process.
    # Just like CSV, inform the user and return to the Create File menu.
    if os.path.exists(check):
        print("File already exists.")
        return

    print("Select the number of key-value pairs (1-10).")

    while True:
        choice = input("Enter Number : ")

        if choice.isdigit() and 1 <= int(choice) <= 10:
            number = int(choice)
            break

        print("Invalid input. Enter a number from 1-10.")

    data = {}

    for i in range(number):
        key = input(f"Enter Key {i + 1} : ")
        value = input(f"Enter Value {i + 1} : ")
        data[key] = value

    with open(check, "w") as f:
        json.dump(data, f, indent=4)

    print("JSON File Created Successfully!")

    while True:
        print("\n--- JSON Menu ---")
        print("1. Add Key-Value Pairs")
        print("2. View File")
        print("3. Back To Menu")

        choice = input("Choose : ")

        if choice == "1":
            with open(check, "r") as f:
                data = json.load(f)

            while True:
                number = input("How many key-value pairs do you want to add? (1-10) ")

                if number.isdigit() and 1 <= int(number) <= 10:
                    number = int(number)
                    break

                print("Invalid input. Enter a number from 1-10.")

            for i in range(number):
                key = input(f"Enter Key {i + 1} : ")
                value = input(f"Enter Value {i + 1} : ")
                data[key] = value

            with open(check, "w") as f:
                json.dump(data, f, indent=4)

            print("Information Added Successfully!")

        elif choice == "2":
            try:
                with open(check, "r") as f:
                    data = json.load(f)

                print("\n--- JSON File Data ---")
                print(json.dumps(data, indent=4))

            except json.JSONDecodeError:
                print("Error: The JSON file contains invalid JSON data.")

            except FileNotFoundError:
                print("File not found.")

        elif choice == "3":
            break

        else:
            print("Invalid Input.")


# ---------------- CREATE FILE ----------------

def create_file():
    while True:
        print("\n--- Select The File Category ---")
        print("1. Python File")
        print("2. CSV File")
        print("3. JSON File")
        print("4. TEXT File")
        print("5. Back To Menu")

        choice = input("Choose : ")

        if choice == "1":
            file_name = input("Enter File Name : ")
            check = file_name + ".py"

            if os.path.exists(check):
                print("File already exists.")
                print("Try a different name.")
                continue

            file_input = input("Enter File Input : ")

            with open(check, "w") as f:
                f.write(file_input + "\n")

            print("Python File Created Successfully!")

            print("1. View File")
            print("2. Back To Menu")
            view_choice = input("Choose : ")

            if view_choice == "1":
                with open(check, "r") as f:
                    print(f.read())

        elif choice == "2":
            csv_menu()

        elif choice == "3":
            json_menu()

        elif choice == "4":
            file_name = input("Enter File Name : ")
            check = file_name + ".txt"

            if os.path.exists(check):
                print("File already exists.")
                print("Try a different name.")
                continue

            text = input("Enter Text : ")

            with open(check, "w") as f:
                f.write(text + "\n")

            print("Text File Created Successfully!")

            print("1. View File")
            print("2. Back To Menu")
            view_choice = input("Choose : ")

            if view_choice == "1":
                with open(check, "r") as f:
                    print(f.read())

        elif choice == "5":
            break

        else:
            print("Invalid Input. Please enter 1-5.")


# ---------------- OPEN FILE ----------------

def open_file():
    extensions = {
        "1": ".py",
        "2": ".csv",
        "3": ".json",
        "4": ".txt"
    }

    while True:
        print("\n--- Select File Type ---")
        print("1. Python File")
        print("2. CSV File")
        print("3. JSON File")
        print("4. TEXT File")
        print("5. Back To Menu")

        choice = input("Enter : ")

        if choice == "5":
            break

        if choice not in extensions:
            print("Invalid Input.")
            continue

        file_name = input("Enter File Name : ")
        file = file_name + extensions[choice]

        if not os.path.exists(file):
            print("File Not Found")
            continue

        try:
            if choice == "1" or choice == "4":
                with open(file, "r") as f:
                    print(f.read())

            elif choice == "2":
                with open(file, "r", newline="") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(row)

            elif choice == "3":
                with open(file, "r") as f:
                    data = json.load(f)
                    print(data)

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print("Could not read the file:", e)


# ---------------- DELETE FILE ----------------

def delete_file():
    extensions = {
        "1": ".py",
        "2": ".csv",
        "3": ".json",
        "4": ".txt"
    }

    while True:
        print("\n--- Select File Type ---")
        print("1. Python File")
        print("2. CSV File")
        print("3. JSON File")
        print("4. TEXT File")
        print("5. Back To Menu")

        choice = input("Enter : ")

        if choice == "5":
            break

        if choice not in extensions:
            print("Invalid Input.")
            continue

        file_name = input("Enter File Name : ")
        file = file_name + extensions[choice]

        if not os.path.exists(file):
            print("File Not Found")
            continue

        confirm = input(f"Delete '{file}'? (y/n) : ").lower()

        if confirm == "y":
            os.remove(file)
            print("File Removed Successfully!")
        else:
            print("Delete Cancelled.")


# ---------------- RENAME FILE ----------------

def rename_file():
    extensions = {
        "1": ".py",
        "2": ".csv",
        "3": ".json",
        "4": ".txt"
    }

    while True:
        print("\n--- Select Current File Type ---")
        print("1. Python File")
        print("2. CSV File")
        print("3. JSON File")
        print("4. TEXT File")
        print("5. Back To Menu")

        choice = input("Enter : ")

        if choice == "5":
            break

        if choice not in extensions:
            print("Invalid Input.")
            continue

        old_name = input("Enter Current File Name : ")
        extension = extensions[choice]
        old_file = old_name + extension

        if not os.path.exists(old_file):
            print("File Not Found")
            continue

        new_name = input("Enter New File Name : ")
        new_file = new_name + extension

        if os.path.exists(new_file):
            print("A file with the new name already exists.")
            continue

        os.rename(old_file, new_file)
        print("File Name Changed Successfully!")


# ---------------- SHOW FILES ----------------

def show_files():
    items = os.listdir()

    print("\n--- Files & Folders ---")

    if not items:
        print("No files or folders found.")
        return

    for item in items:
        if os.path.isdir(item):
            print("[Folder]", item)
        else:
            print("[File]  ", item)


# ---------------- MAIN MENU ----------------

while True:
    print("\n      ««« FILE MANAGER »»»")
    print("____________ MENU ____________")
    print("|  1. Create New File         |")
    print("|  2. Open File               |")
    print("|  3. Delete File             |")
    print("|  4. Rename File             |")
    print("|  5. Show Existing Files     |")
    print("|  6. Exit                    |")
    print("——————————————————————————————")

    choice = input("Choose : ")

    if choice == "1":
        create_file()

    elif choice == "2":
        open_file()

    elif choice == "3":
        delete_file()

    elif choice == "4":
        rename_file()

    elif choice == "5":
        show_files()

    elif choice == "6":
        print("Program Finished")
        break

    else:
        print("Invalid Input. Please enter 1-6."
