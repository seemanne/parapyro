import os
from pathlib import Path

class Tectonic():

    def __init__(self) -> None:
        pass

    def render(self, filename):
        
        os.system(f"""tectonic compiled_files/raw/{filename}.tex -o "compiled_files/" """)