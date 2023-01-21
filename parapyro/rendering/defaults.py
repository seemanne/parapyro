from parapyro.utils.compiler_utils import set_in_brackets, preempt_slash

class DefaultStyle():

    def __init__(self) -> None:
        pass

    def _generate_frontmatter(self):

        return f"""
{preempt_slash("usecolortheme")}{set_in_brackets("dove")}
"""

class DefaultTemplate():

    def __init__(self) -> None:
        pass

    def _generate_frontmatter(self):

        return ""