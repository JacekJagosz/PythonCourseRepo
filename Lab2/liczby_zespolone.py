class ComplexNumber:
    def __init__(self, real, imag=0.0):
        """
        Initialize a ComplexNumber instance.

        Args:
            real (float): The real part of the complex number.
            imag (float): The imaginary part of the complex number.
        """
        self.real = float(real)
        self.imag = float(imag)

    def __add__(self, other):
        """
        Add two ComplexNumber instances or a ComplexNumber and a numeric value.

        Args:
            other (ComplexNumber or float): The value to add.

        Returns:
            ComplexNumber: The result of addition.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real + other, self.imag)
        else:
            raise TypeError("Unsupported operand type(s) for +.")

    def __sub__(self, other):
        """
        Subtract a ComplexNumber or numeric value from this ComplexNumber.

        Args:
            other (ComplexNumber or float): The value to subtract.

        Returns:
            ComplexNumber: The result of subtraction.
        """
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return ComplexNumber(self.real - other, self.imag)
        else:
            raise TypeError("Unsupported operand type(s) for -.")

    def __str__(self):
        """
        String representation of the ComplexNumber instance.

        Returns:
            str: String representation in the form "a + bi" or "a - bi".
        """
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


num1 = ComplexNumber(3, 4)  # 3 + 4i
num2 = ComplexNumber(1, -2)  # 1 - 2i

# Dodawanie
result_add = num1 + num2
print("Dodawanie:", result_add)

# Odejmowanie
result_sub = num1 - num2
print("Odejmowanie:", result_sub)

result_add_real = num1 + 5
print("Dodaj liczbę rzeczywistą:", result_add_real)

result_sub_real = num1 - 2
print("Odejmij liczbę rzeczywistą:", result_sub_real)
