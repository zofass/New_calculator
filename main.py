while True:
    try:
        first_value = int(input("Please enter first number: "))
        action = input("Please enter action: ")
        second_value = int(input("Please enter second number: "))

        result = None

        if action == '+':
            result = first_value + second_value
        elif action == '-':
            result = first_value - second_value
        elif action == '*':
            result = first_value * second_value
        elif action == '/':
            if second_value != 0:
                result = first_value / second_value
            else:
                print("You can't divide by 0")
                continue

        print("Your result is:", result)

        continue_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if continue_calculation not in {'yes', 'y'}:
            break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

