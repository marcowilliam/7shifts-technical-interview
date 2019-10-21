import re

class Calculator:

    def add(self, numbers):
        if numbers.strip():
            splitted_numbers = self.split_numbers(numbers)
            self.check_negative_numbers(splitted_numbers)
            valid_numbers = [number for number in splitted_numbers if number <= 1000]
            return sum(valid_numbers)
        else:
            return 0
    
    def split_numbers(self, numbers):
        delimiter_found = re.search('//(.*)\n', numbers)
        if delimiter_found:
            delimiter_grouped = delimiter_found.group(1)
            delimiters = re.escape(delimiter_grouped).replace("\,", "|")
            numbers_to_add = numbers.split("\n", 1)[1]
            return map(int, re.split(delimiters, numbers_to_add))
        else:
            return map(int, numbers.split(","))
    
    def check_negative_numbers(self, numbers):
        negative_numbers = [number for number in numbers if number < 0]
        if negative_numbers:
            raise NegativesNotAllowed(negative_numbers)

class NegativesNotAllowed(Exception):

     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)  
            
if __name__ == '__main__':
    numbers = input("Enter string of numbers: ")
    print Calculator().add(numbers)
