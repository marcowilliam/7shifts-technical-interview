import re

class Calculator:

    def add(self, numbers):
        if numbers.strip():
            delimiter_found = re.search('//(.*)\n', numbers)
            if delimiter_found:
                delimiter_grouped = delimiter_found.group(1)
                delimiters = re.escape(delimiter_grouped).replace("\,", "|")
                numbers_to_add = numbers.split("\n", 1)[1]
                splitted_numbers = map(int, re.split(delimiters, numbers_to_add))
            else:
                splitted_numbers = map(int, numbers.split(","))
            
            negative_numbers = [number for number in splitted_numbers if number < 0]
            if not negative_numbers:
                valid_numbers = [number for number in splitted_numbers if number <= 1000]
                return sum(valid_numbers)
            else:
                raise NegativesNotAllowed(negative_numbers)  
        else:
            return 0

class NegativesNotAllowed(Exception):

     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)  
            
if __name__ == '__main__':
    numbers = input("Enter string of numbers: ")
    print Calculator().add(numbers)
