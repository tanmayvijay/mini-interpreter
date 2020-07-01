import re

def tokenizer(string: str):
    token_rexes = [
        (re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*"), "iden"), # variables
        (re.compile(r"^[0-9]+"), "num"), # integers
        (re.compile(r"^[+*/-]"), "op"), # operators
        (re.compile(r"^[()]"), "paran"), # parantehses
        (re.compile(r"^="), "ass"), # assignment
    ]

    tokens = []

    while len(string):
        string = string.lstrip()

        matched = False

        for token_rex, token_type in token_rexes:
            mo = token_rex.match(string)
            if mo:
                matched = True
                token = (mo.group(0), token_type)
                tokens.append(token)
                string  = token_rex.sub('', string)
                string = string.lstrip()
                break # break out of the inner loop
        
        if not matched:
            raise Exception("Invalid String")
    
    return tokens

