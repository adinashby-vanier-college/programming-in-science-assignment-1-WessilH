# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    numbers = [num1, num2, num3,] 
    max_value = max(numbers)
    return (max_value)

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    min_value= min(num1,num2,num3)
    return min_value

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number ==0:
        return "Zero"
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"



# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(n):
    result = ""
    
    if n % 2 == 0:
        return "The number should be odd"
    
    for i in range (n):
        for j in range (i+1):
            result += "*"
        result = result.rstrip()
        result += "\n"

    return (result.rstrip())

        
# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(n):
    result = ""

    for i in range(1, n + 1):
        if i % 3 == 0:
            result += "Multiple of 3"
            result += "\n"  
        else:
            result += str(i)
            result += "\n"

    return result.rstrip()
       


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    result = 0
    
    for i in range (start, end+1):
        if i % 2 == 0:
            result += i
  
    return result
    
