from parapyro.utils.compiler_utils import preempt_slash, stack_list_to_lines, begin, end, to_latex_bool, set_in_brackets
from parapyro import PROJECT_HOME
from matplotlib.figure import Figure

class BaseObject():
    
    def __init__(self, name) -> None:

        self.name = name

    def compile(self):

        raise NotImplementedError(f"Object does not implement compile()")

    def get_name(self):

        return self.name

class ImageObject():

    def __init__(self, name, filepath) -> None:
        
        self.filepath = filepath

        super.__init__(name)

    def _figure_from_file(self, **kwargs):
        
        box_params = {
            "width" : 16,
            "height" : 9,
            "keepaspectratio" : True
        }
        box_params.update(kwargs)
        output = ""
        lines_list = [
            f"{begin('figure')}",
            f"{preempt_slash('centering')}",
            f"{preempt_slash('includegraphics')}[width={str(box_params['width'])}cm, height={str(box_params['height'])}cm, keepaspectratio={to_latex_bool(box_params['keepaspectratio'])}]{set_in_brackets(self.filepath)}",
            f"{end('figure')}"
        ]
        output += stack_list_to_lines(lines_list)

        return output

    def compile(self, **kwargs):

        return self._figure_from_file(**kwargs)


def imageobject_from_pyplot(fig: Figure, name):

    fig.savefig(PROJECT_HOME / f"compiled_files/raw/{name}.png")
    return ImageObject(name, f"compiled_files/raw/{name}.png")