# Simple Calculator
# Function for addition of two values
def add(x,y):
    return x + y
# Function for Subscraction of two numbers
def sub(x,y):
    return x - y
# Function for multiplication of two numbers.
def multiply(x,y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else: 
        print("Division with {y} is not allowed. ")

def calculator():
    print("...........Simple Calculator............")
    print("\n \n.........Select An Operation........")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("q: Quit the Calculator")


    while True:
        try:
        # User input: Ask user to select Operation
            choice = input("Select Operation from 1 to 4: or Select 'q' for quit.")
        # Operation to quite the program
            if choice == 'q':
                print("Existing the Calcultor, Goodbye")
                break
            if choice in ["1", "2", "3", "4"]:
                num1 = float(input("Enter your first Number (x): "))
                num2 = float(input("Enter Your Secod Number (y): "))
                if choice == '1':
                    print(f" {num1} + {num2} = ", add(num1, num2))
                elif choice == '2':
                    print(f"{num1} - {num2} = ", sub(num1,num2))
                elif choice == '3':
                    print(f" {num1} x {num2} = ", multiply(num1,num2) )
                elif choice == '4':
                    print(f" {num1} / {num2} = ", divide(num1,num2))
            else:
                print("Invalid Input: Please select Valid Number.")
        except ValueError:
            print("Invalid Choice: Please Read Information Carefully and select 1-4 Number for operation or 'q for Quit the Calculator.")

# Run The Calculator
if __name__ == "__main__":
    calculator()




