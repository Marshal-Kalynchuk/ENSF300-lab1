def myMul(a, b):
    return a * b
def myDiv(a, b):
    return a // b
def myAdd(a, b):
    return a +  b
def mySub(a, b):
    return a - b

def validation(program_input, input_type, input_position, previous_input): #this function needs two string inputsinputs
    input_valid = False #used in checking validity of input
    operators_list = ["*","/","-","+"] #lsits of valid responses
    digits_list = ["0","1","2","3","4","5","6","7","8","9"]

    while input_valid == False: #false on first encounter, runs validity loop

        if input_type == 0: #input 0 is for digits
            for i in program_input: #iterates over string length
                if i in digits_list: #iterates each character in string
                    input_valid = True #sets as true, all characters must be true for the function to exit the validation loop
                else: #if not valid
                    input_valid = False #returns the validity statement to false in the case that the input becomes true
                    break
        
        if input_type == 1: #input  1 is for operators
                if program_input in operators_list: #if input is in valid list
                    input_valid = True #sets as true
                else: #if not valid
                    input_valid = False #returns the validity statement to false in the case that input_valid became true

        if input_position in [3,5]:
            while program_input == "0":
                if input_position == 3 and previous_input == "/" and program_input == "0":
                    print("Your input is invalid. You cannot divide by zero.\n")
                    program_input = input("Please enter a valid number: ") #requests an input
                    input_valid = False
                if input_position == 5 and previous_input == "/" and program_input == "0":
                    print("Your input is invalid. You cannot divide by zero.\n")
                    program_input = input("Please enter a valid number: ") #requests an input
                    input_valid = False

        if input_valid == False and input_type == 0: #if the number is not valid the program asks for more input
            print("Your input is invalid. Please input a number.\n")
            program_input = input("Please enter a valid number: ") #requests an input
        if input_valid == False and input_type ==1: #if the operator is not valid the program asks for more input
            print("Your input is invalid. Please input an operator.\n")
            program_input = input("Please enter a valid operator: ") #requests an input       

    if input_valid == True and input_type == 0: #sets the program_input as an interger if its a digit
        program_input = int(program_input)

    return program_input #returns a valid value, it is a string if its an operator and a interger if it is a number.

def evaluate (operations,operands):
    result = 0
    if (operations[0] == "*"):
        result = myMul(operands[0],operands[1])
        return result
    elif (operations[0] == "/"):
        result = myDiv(operands[0],operands[1])
        return result   
    elif(operations[1] == "*"):
        result = myMul(operands[1],operands[2])
        return result
    elif(operations[1] == "/"):
        result = myDiv(operands[1],operands[2])
        return result
    if(operations[1] == "*"):
        result = myMul(result,operands[2])
        return result
    elif(operations[1] == "/"):
        result = myDiv(result,operands[2])
        return result
    if (operations[0] == "+"):
        result = myAdd(operands[0],operands[1])
        return result
    elif (operations[0] == "-"):
        result = mySub(operands[0],operands[1])
        return result
    if (operations[1] == "+"):
        result = myAdd(result,operands[2])
        return result
    elif (operations[1] == "-"):
        result = mySub(result,operands[2])
        return result
    return result
def display(operations,operands,result):
    print("{} {} {} {} {} = ".format(operands[0],operations[0],operands[1],operations[1],operands[2]))
    print(result)

def main():
    first_number_input = str(input('Please enter the first number: '))
    first_number = validation(first_number_input,0,1,0)

    first_operator_input = str(input('Please enter the first operator: '))
    first_operator = validation(first_operator_input,1,2,first_number)

    second_number_input = str(input('Please enter the second number: '))
    second_number = validation(second_number_input,0,3, first_operator)
    
    second_operator_input = str(input('Please enter the second operator: '))
    second_operator = validation(second_operator_input,1,4,second_number)

    third_number_input = str(input('Please enter the third number: '))
    third_number = validation(third_number_input,0,5,second_operator)

if __name__ == "__main__":
    main()