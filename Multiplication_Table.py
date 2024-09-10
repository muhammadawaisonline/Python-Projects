def multiplication_table(number, limit):
    print(f"Multiplication Table for {number} upto {limit}")
    for i in range(1, limit + 1):
        result =  number * i
        print(f" {number} x {i} = {result}")

def main():
    while True:    
        try:
            number = int(input("Enter Your Table Number: "))
            limit = int(input("Enter the Limit Number of the Table: "))

            multiplication_table(number, limit)
        except ValueError:
            print("InValid Input: Enter Valid Number for Table and Limit.")


if __name__ == "__main__":
    main()