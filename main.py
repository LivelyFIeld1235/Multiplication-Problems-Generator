import random

# Function to generate multiplication problems
def generate_multiplication_problems(start, end, num_problems):
    problems = []
    for _ in range(num_problems):
        x = random.randint(start, end)
        n = random.randint(1, 20)
        result = x * n
        problems.append(f"{n} x {x} = {n*x}")
    return problems

# Get user input for the range and number of problems
start = int(input("Enter the start number for the range: "))
end = int(input("Enter the end number for the range: "))
num_problems = 640  # You can change this number if needed

# Generate multiplication problems
problems = generate_multiplication_problems(start, end, num_problems)

# Display the multiplication problems in the console
counter = 0
while counter != problems.index(problems[-1]):
    if counter%8 == 7: 
        print(problems[counter])
        print("\n")
        counter += 1;
    else:
        print(problems[counter], end = "              ")
        counter += 1;