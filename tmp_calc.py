# make a REPL function 
# example below:
# do_setup()
# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print output
# pseudocode for this exercise:
# No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is 'q', quit
#     otherwise decide which math function to call based on the tokens we read
import arithmetic

print """Welcome to our prefix calculator!
Please enter an operation first, then the number
or numbers you would like to calculate.
enter an operator from the following:
+ - * / square cube power mod
Enter 'q' to quit calculator
"""

while True:

    input = raw_input(">")
    tokens = input.split(" ")

    if tokens[0] == "q":
        break
    
    if (tokens[0].isalpha() or tokens[1].isalpha() or tokens[2].isalpha()) and tokens[0] not in ["cube", "square", "power", "mod"]:
        print "Sorry, that is not a valid entry. \n Please enter a valid operator followed by a number or numbers"

    else:
        
        num1 = float(tokens[1])
        if tokens[0] != "cube" and tokens[0] != "square" and tokens[0] != "q": 
            num2 = float(tokens[2])

        if tokens[0] == "+":
            print arithmetic.add(num1, num2)

        if tokens[0] == "-":
            print arithmetic.subtract(num1, num2)

        if tokens[0] == "*":
            print arithmetic.multiply(num1, num2)

        if tokens[0] == "/":
            print float(arithmetic.divide(num1, num2))

        if tokens[0] == "square":
            print arithmetic.square(num1)

        if tokens[0] == "cube":
            print arithmetic.cube(num1)

        if tokens[0] == "power":
            print arithmetic.power(num1, num2)

        if tokens[0] == "mod":
            print arithmetic.power(num1, num2)



