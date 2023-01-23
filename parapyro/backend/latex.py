import os
from pathlib import Path
from parapyro.backend.base_backend import BaseBackend

class Pdftex(BaseBackend):

    def __init__(self) -> None:
        pass

    def render(self, filename):
        
        os.system(f"""pdflatex compiled_files/raw/{filename}.tex --output-directory "compiled_files/" """)