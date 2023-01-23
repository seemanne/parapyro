import os
from pathlib import Path
from parapyro.backend.base_backend import BaseBackend

class Tectonic(BaseBackend):

    def __init__(self) -> None:
        pass

    def render(self, filename):
        
        os.system(f"""tectonic compiled_files/raw/{filename}.tex -o "compiled_files/" """)