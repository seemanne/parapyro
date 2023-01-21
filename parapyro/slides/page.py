from parapyro.utils.compiler_utils import set_in_brackets, preempt_slash

class Page():

    def __init__(self, title, content: str ="") -> None:
        
        self.title = title
        self.content = content

    def compile(self):

        output = ""
        output += f"""
{preempt_slash("begin")}{set_in_brackets("frame")}
{preempt_slash("frametitle")}{set_in_brackets(self.title)}
"""
        output += self.content
        output += f"""
{preempt_slash("end")}{set_in_brackets("frame")}
"""
        return output