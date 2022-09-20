def myMul(a, b):
    return a * b
def myDiv(a, b):
    return a // b
def myAdd(a, b):
    return a +  b
def mySub(a, b):
    return a - b

def main():
    first_number_input = str(input('Please enter the first number'))
    first_number = validation(first_number_input,0)

    first_operator_input = str(input('Please enter the first operator'))
    first_operator_input = validation(first_operator_input,1)

    second_number_input = str(input('Please enter the second number'))
    second_number = validation(second_number_input,0)
    
    second_operator_input = str(input('Please enter the second operator'))
    second_operator_input = validation(second_operator_input,1)

    third_number_input = str(input('Please enter the third number'))
    third_number = validation(third_number_input,0)
    
if __name__=='__main__':
    main()