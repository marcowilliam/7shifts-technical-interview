class Calculator:

    def add(self, numbers):
        if numbers.strip():
            splitted_numbers = map(int, numbers.split(","))
            return sum(splitted_numbers)
        else:
            return 0
            
if __name__ == '__main__':
    numbers = input("Enter string of numbers: ")
    print Calculator().add(numbers)
