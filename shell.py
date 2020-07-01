from tokenizer import tokenizer
from mini_parser import mini_parser

print("Mini Interpreter\n")

while(True):
    try:

        input_ = input(">> ")

        # tokenize
        tokens = tokenizer(input_)

        # parser
        output = mini_parser(tokens)

        if output:
            print(output)
    except KeyboardInterrupt:
        exit()