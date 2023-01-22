

def set_in_brackets(input: str, brackets: list= ["{", "}"]):
    return brackets[0] + input + brackets[1]

def preempt_slash(input: str):
    return "\\" + input

def usepackage(input:str):
    return f"{preempt_slash('usepackage')}{set_in_brackets(input)}"

def stack_list_to_lines(lines: list):

    output = ""
    for line in lines:
        output += line + "\n"
    return output