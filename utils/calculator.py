class Calculator:
    def add(self, a, b):
        """
        Returns the sum of a and b.

        Args:
            a (float): The first addend.
            b (float): The second addend.

        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Returns the difference between a and b.

        Args:
            a (float): The minuend.
            b (float): The subtrahend.

        Returns:
            float: The difference of a and b.
        """

        return a - b

    def multiply(self, a, b):
        """
        Returns the product of a and b.

        Args:
            a (float): The multiplicand.
            b (float): The multiplier.

        Returns:
            float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Returns the quotient of a and b.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The quotient of a and b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return a / b
