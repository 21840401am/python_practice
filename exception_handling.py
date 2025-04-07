number = int(input("Enter a number: "))
result = 10 / number
print(result)

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed!")



try:
    number = int(input("Enter a number: "))
    result = 10 / number
except Exception as e:
    print(f"You got this error {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed!")









