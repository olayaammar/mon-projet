def factoriel(X):
    if X == 0 or X == 1:
        return 1
    else:
        return X * factoriel(X - 1)

# Ask the user for a number
num = int(input("Please enter a valid number: "))

# Print the factorial
print(f"The factorial of {num} is {factoriel(num)}")