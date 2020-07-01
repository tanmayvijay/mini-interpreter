# Symbol Table
from .symbol_table import SymbolTable

# Precedence Mapping:
precedence = {
    "-": 1,
    "+": 2,
    "*": 3,
    "/": 4,
}

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

operator_mapping = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}



def parse_expr(tokens: list):
    # Shunting Yard Algorithm

    operator_stack = []
    expression_stack = []

    tokens.append( (')', "paran") )

    i = 0
    while i < len(tokens):
        token = tokens[i]

        if token[0] == "(":
            value, tokens = parse_expr(tokens[i+1:])
            i = -1
            
            expression_stack.append(value)

        elif token[1] == "num":
            expression_stack.append(float(token[0]))

        elif token[1] == "iden":
            value = SymbolTable.find_symbol(token[0])
            expression_stack.append(float(value))

        elif token[1] == "op":
            # Shunting yard
            while len(operator_stack) and precedence[token[0]] < precedence[operator_stack[-1]]:
                operator = operator_stack.pop()
                operand_2 = expression_stack.pop()
                operand_1 = expression_stack.pop()

                value = operator_mapping[operator] (operand_1, operand_2)
                expression_stack.append(value)

            operator_stack.append(token[0])

        elif token[0] == ")":
            while len(operator_stack):
                operator = operator_stack.pop()
                operand_2 = expression_stack.pop()
                operand_1 = expression_stack.pop()

                value = operator_mapping[operator] (operand_1, operand_2)
                expression_stack.append(value)
            
            return expression_stack[-1], tokens[i+1:-1]
        
        i += 1




def parse_ass(tokens: list):
    name = tokens[0][0]
    value = tokens[2:]
    value, tokens = parse_expr(value)

    SymbolTable.add_symbol(name, value)


def mini_parser(tokens: list):
    # assignment statement
    if tokens[1][0] == "=":
        parse_ass(tokens)
    else: # expressions
        return parse_expr(tokens)[0]