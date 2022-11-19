def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2


print("Hi, I am a Calculator!")
print("Please select which of the following arithematic operation you want me to perform-\n" \
    "1. Add\n" \
    "2. Subtract\n" \
    "3. Multiply\n" \
    "4. Divide\n")

operation = int(input(" 1, 2, 3, or 4 :"))

number_1 = int(input('Please, Enter the first number: '))
number_2 = int(input('Please, Enter the second number: '))

if operation == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif operation == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif operation == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))

elif operation == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))

else:
    print("Please enter Valid input")