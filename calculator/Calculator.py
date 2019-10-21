import re

class Calculator:

    def add(self, numbers):
        if numbers.strip():
            delimiter_found = re.search('//(.*)\n', numbers)
            if delimiter_found:
                delimiter = delimiter_found.group(1)
                numbers_to_add = numbers.split("\n")[1]
                splitted_numbers = map(int, numbers_to_add.split(delimiter))
            else:
                splitted_numbers = map(int, numbers.split(","))
            
            negative_numbers = [number for number in splitted_numbers if number < 0]
            if negative_numbers:
                raise NegativesNotAllowed(negative_numbers)
            else:
                return sum(splitted_numbers)
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
