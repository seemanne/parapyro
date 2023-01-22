import os
from pathlib import Path
from parapyro.rendering.defaults import DefaultStyle, DefaultTemplate
from parapyro.backend.tectonic import Tectonic
from parapyro.slides.page import Page
from parapyro.slides.object import BaseObject
from parapyro.utils.compiler_utils import set_in_brackets, preempt_slash, usepackage, stack_list_to_lines




class Presentation():

    def __init__(self, filename, style=None, template=None, backend=None, **kwargs) -> None:
        
        if style:
            self.style = style
        else:
            self.style = DefaultStyle()

        if template:
            self.template=template
        else:
            self.template = DefaultTemplate()
        
        if backend:
            self.backend=backend
        else:
            self.backend = Tectonic()

        default_params = {
            "title" : "Presentation title",
            "author" : "Presentation author",
            "institute" : "Author institute",
            "fontsize" : "17",
            "aspectratio" : "169",
        }
        self.params = default_params
        self.params.update(kwargs)
        self.page_store = []
        self.object_store = {}
        self.filename = filename

    def add_page(self, page: Page):

        self.page_store.append(page)

    def add_object(self, object: BaseObject, force_overwrite= False):

        name = object.name
        if self.object_store.get(name, False) and not force_overwrite:
            raise KeyError("Object name must be unique, force an override by passing `force_overwrite=True` to add_object")
        
        self.object_store[name] = object
    

    def compile(self):

        output = ""
        output += self._generate_frontmatter()

        for page in self.page_store:
            output += page.compile()
        
        output += self._generate_backmatter()

        self.raw_output = output

        self._save_tex()

    def render(self):

        self.backend.render(self.filename)

    def _generate_frontmatter(self):

        output = ""
        preamble_list = [
            f"\documentclass[{self.params['fontsize']}pt, aspectratio={self.params['aspectratio']}]{set_in_brackets('beamer')}",
            f"{usepackage('graphicx')}",
            f"{preempt_slash('title')}{set_in_brackets(self.params['title'])}",
            f"{preempt_slash('author')}{set_in_brackets(self.params['author'])}",
            f"\institute{set_in_brackets(self.params['institute'])}",
        ]
        output += stack_list_to_lines(preamble_list)
        output += self.style._generate_frontmatter()
        output += self.template._generate_frontmatter()
        frontmatter_list = [
            f"{preempt_slash('begin')}{set_in_brackets('document')}",
            f"{preempt_slash('frame')}{set_in_brackets(preempt_slash('titlepage'))}"
        ]
        output += stack_list_to_lines(frontmatter_list)

        return output

    def _generate_backmatter(self):

        output = ""
        output += "\end{document}"
        return output


    def _save_tex(self):

        print(self.raw_output)
        path_str = os.getcwd()
        path = Path(path_str)
        savedir = path / "compiled_files/raw"
        savedir.mkdir(parents=True, exist_ok = True)
        with open(savedir / f"{self.filename}.tex", "w") as file:
            file.write(self.raw_output)

if __name__ == "__main__":

    pres = Presentation("test_name")
    pres.add_page(Page("example page", "oh this content is nasty good yes"))
    pres.compile()
    pres.render()