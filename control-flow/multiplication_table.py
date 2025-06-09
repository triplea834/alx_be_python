# multiplication_table.py

# Step 1: Prompt the user for a number and convert the input to an integer
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")