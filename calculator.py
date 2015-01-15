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

input = raw_input(">")
tokens = input.split(" ")
num1 = int(tokens[1])
num2 = int(tokens[2])

if tokens[0] == "+":
    print arithmetic.add(num1, num2)

if tokens[0] == "-":
    print arithmetic.subtract(num1, num2)

if tokens[0] == "*":
    print arithmetic.multiply(num1, num2)

if tokens[0] == "/":
    print arithmetic.divide(num1, num2)

if tokens[0] == "square":
    print arithmetic.square(num1)

if tokens[0] == "cube":
    print arithmetic.cube(num1)

if tokens[0] == "power":
    print arithmetic.power(num1, num2)

if tokens[0] == "mod":
    print arithmetic.power(num1, num2)
