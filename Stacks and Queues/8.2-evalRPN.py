# A string is said to be an expression in RPN (reverse polish notation) if
# it is a single digit or sequence prefixed with an option -
# and it is the form A, B, o where A and B are RPN expressions and o
# is one of +, -, x, /. For example, the following strings:
# "1729", "3,4,+,2,x,1,+", "-641,6,/,28,/"

# RPN expression can be evaluated uniquely to an integer, which is
# determined recursively. 

# Write a program that takes an arithmetical expression in RPN and returns the
# number that the expression evaluates to.

# EPI solution

def evaluate(RPN_expression):
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y, '*':
        lambda y, x: x * y, '/': lambda y, x: int(x/y)
    }

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token](
                intermediate_results.pop(), intermediate_results.pop()))
        else: # token is a number
            intermediate_results.append(int(token))
    return intermediate_results[-1]

# anexp = "6,5,+"
# print(evaluate(anexp))
# Uses O(1) computation time per char, so time complexity is O(n), where 
# n is length of string. Space is based on size of expression, O(n)

# Solve the same problem for expressions in Polish notation,
# When A, B, o is replaced by o, A, B in Rule 2.

def evaluatePN(RPN_expression):
    intermediate_results = []
    current_operator = ''
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y, '-': lambda y, x: x - y, '*':
        lambda y, x: x * y, '/': lambda y, x: int(x/y)
    }
    first_indicator = True
    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS and first_indicator == True:
            current_operator = token
            first_indicator = False
        elif token in OPERATORS and first_indicator == False:
            intermediate_results.append(OPERATORS[current_operator](
                intermediate_results.pop(), intermediate_results.pop()))
            current_operator = token
        else: # token is a number
            intermediate_results.append(int(token))
    intermediate_results.append(OPERATORS[current_operator](
                intermediate_results.pop(), intermediate_results.pop()))
    return intermediate_results[-1]

anexp = "+,6,5,-,5,+,10,/,4"
print(evaluatePN(anexp))