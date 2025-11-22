class Calculator:
    # The constructor: save the two numbers and the operation name
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    # Do the chosen operation and return the result or an error message
    def calculate(self):
        if self.operation == "add":
            result = self.a + self.b
            return result

        elif self.operation == "sub":
            result = self.a - self.b
            return result

        elif self.operation == "mul":
            result = self.a * self.b
            return result

        elif self.operation == "div":
            if self.b == 0:
                return "Cannot divide by zero"
            result = self.a / self.b
            return result

        else:
            return "Invalid operation"


# --- Get input from the user ---
# We use float so 'a' and 'b' are treated as double-type numbers
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add / sub / mul / div): ")

# --- Create calculator object and get result ---
calc = Calculator(a, b, operation)
answer = calc.calculate()

# --- Show the result ---
print("Result:", answer)

