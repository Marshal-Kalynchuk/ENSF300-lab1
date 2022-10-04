def myMul(a, b):
    """
    This funtion multiplies two numbers (a and b) that are given in the parameter
    parameter a: First number
    parameter b: Second number 
    return multiplication operation result

    """ 
    return a * b
def myDiv(a, b):
    """
    This funtion divides a number by b number, both of these numbers are giving in the parameter
    parameter a: First number
    parameter b: Second number 
    return division operation result

    """ 
    return a // b
def myAdd(a, b):
    """
    This funtion adds two numbers a and b that are giving in the parameter
    parameter a: First number
    parameter b: Second number 
    return addition operation result

    """ 
    return a + b
def mySub(a, b):
    """
    This funtion substracts b number from a number which are giving in the parameter
    parameter a: First number
    parameter b: Second number 
    return substraction operation result

    """ 
    return a - b

def validation(program_input, input_type, input_position, previous_input): #this function needs four inputs
    #program_input is a string parameter of the user input
    #input_type is a interger that determines if the input is supposed to be a number or a operator
    #input_position is a interger thqt represents the position of the input in the equation
    #previous_input is the verfifed input of the previous position in the equation
    #this function returns a string if the input is in the operator position or a interger if the input is in the number position 

    input_valid = False #used in checking validity of input
    operators_list = ["*","/","-","+"] #lists of valid responses
    digits_list = ["0","1","2","3","4","5","6","7","8","9"] #list of valid responses

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
            if input_position == 3 and previous_input == "/" and program_input == "0" and input_valid == True: #checks if previous input is a division
                print("\nYour input is invalid. You cannot divide by zero.")
                program_input = str(input("Please enter a valid number: ")) #requests an input
                input_valid = False
            if input_position == 5 and previous_input == "/" and program_input == "0" and input_valid == True:#checks if previous input is a division
                print("\nYour input is invalid. You cannot divide by zero.")
                program_input = str(input("Please enter a valid number: ")) #requests an input
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
    if (operations[0] == "*"):                      #If statement to see if the first operator is *
        result = myMul(operands[0],operands[1])     #Uses the myMul function
        if(operations[1] == "*"):                   #If statement to see if the second operator is *
            result =  myMul(result,operands[2])     #Uses the myMul function
        elif(operations[1] == "/"):                 #If else statement to see if the second operator is /
            result =  myDiv(result,operands[2])     #Uses the myDiv function
    elif (operations[0] == "/"):                    #If else statement to see if the first operator is /
        result = myDiv(operands[0],operands[1])     #Uses the myDiv function
        if(operations[1] == "*"):                   #If statement to see if the second operator is *
            result =  myMul(result,operands[2])     #Uses the myMul function
        elif(operations[1] == "/"):                 #If else statement to see if the second operator is /
            result = myDiv(result,operands[2])      #Uses the myDiv function

    elif (operations[0] == "+"):                    #If statement to see if the first operator is +
        if(operations[1] == "*"):                   #If statement to see if the second operator is *
            result = myMul(operands[1],operands[2]) #Uses the myMul function
            result = myAdd(operands[0],result)      #Uses the myAdd function
        elif(operations[1] == "/"):                 #If else statement to see if the second operator is /
            result = myDiv(operands[1],operands[2]) #Uses the myDiv function
            result = myAdd(operands[0],result)      #Uses the myAdd function
        else:                                       
            result =  myAdd(operands[0],operands[1])#Uses the myAdd function
    elif (operations[0] == "-"):                    #If else statement to see if the first operator is -
        if(operations[1] == "*"):                   #If statement to see if the second operator is *
            result = myMul(operands[1],operands[2]) #Uses the myMul function
            result = mySub(operands[0],result)      #Uses the mySub function
        elif(operations[1] == "/"):                 #If else statement to see if the second operator is /
            result = myDiv(operands[1],operands[2]) #Uses the myDiv function
            result = mySub(operands[0],result)      #Uses the mySub function
        else:                                       
            result = mySub(operands[0],operands[1]) #Uses the mySub function
    if (operations[1] == "+"):                      #If statement to see if the second operator is +
        result = myAdd(result,operands[2])          #Uses the myAdd function
    elif (operations[1] == "-"):                    #If else statement to see if the second operator is -
        result = mySub(result,operands[2])          #Uses the mySub function
    return result

def display(operations,operands,result):
    print("{} {} {} {} {} = {}".format(operands[0], operations[0], operands[1], operations[1], operands[2], result)) #Prints the formatted display

def main():
    print("Welcome to the simple calculator. Please enter three digits and two operators into the calculator:") #Prints Welcome Message
    first_number_input = str(input('Please enter the first number: '))                                          #Takes in the input from the user
    first_number = validation(first_number_input,0,1,0)                                                         #Uses the Validation Function to Validates the input

    first_operator_input = str(input('Please enter the first operator: '))      #Takes in the input from The User
    first_operator = validation(first_operator_input,1,2,first_number)          #Uses the Validation Function to Validates the inputs   

    second_number_input = str(input('Please enter the second number: '))        #Takes in the input from The User
    second_number = validation(second_number_input,0,3, first_operator)         #Uses the Validation Function to Validates the inputs
    
    second_operator_input = str(input('Please enter the second operator: '))    #Takes in the input from The User
    second_operator = validation(second_operator_input,1,4,second_number)       #Uses the Validation Function to Validates the inputs

    third_number_input = str(input('Please enter the third number: '))          #Takes in the input from The User
    third_number = validation(third_number_input,0,5,second_operator)           #Uses the Validation Function to Validates the inputs
    operators = [first_operator, second_operator]                               #Creates the list for operators
    operands = [first_number, second_number, third_number]                      #Creates the list for operands

    answer = evaluate(operators, operands)                                      #Uses the Evaluate Function to find the anwser
    display(operators, operands, answer)                                        #Uses the Display Function to display the answer

    
if __name__ == "__main__":
    main()
