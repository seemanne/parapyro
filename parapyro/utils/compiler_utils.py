

def set_in_brackets(input: str, brackets: list= ["{", "}"]):
    return brackets[0] + input + brackets[1]

def preempt_slash(input: str):
    return "\\" + input