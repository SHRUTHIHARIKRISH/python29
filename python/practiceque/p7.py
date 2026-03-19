"""Number Sorting Program

Write a Python program that takes a list of numbers from the user and displays them in ascending and descending order.

"""
a = []

while True:
    print("\n1. ASCENDING ORDER")
    print("2. DESCENDING ORDER")
    print("3. EXIT")

    choice = int(input("Enter an option: "))

    if choice == 3:
        print("Exit")
        break

    b = int(input("Enter the number of elements: "))

    a = []   # clear list for new input

    for i in range(b):
        num = int(input("Enter the number: "))
        a.append(num)

    if choice == 1:
        a.sort()
        print("Ascending order:", a)

    elif choice == 2:
        a.sort(reverse=True)
        print("Descending order:", a)

    else:
        print("Invalid option")






