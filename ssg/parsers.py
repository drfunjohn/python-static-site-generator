from typing import List
from pathlib import Path
import shutil

class Parser:
    """
    parser
    """

    extensions: List[str]= []

    def valid_extension(self, extension):
        """
        check extension type
        """
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        """
        implement in the subclass
        """
        print(f"{self},{path}{dest}{source}")
        raise NotImplementedError

    def read(self, path):
        """
        read content of file
        """
        with open(path, "r") as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        full_path=Path( dest / path.with_suffix(ext).name )
        with open(full_path,"w") as file:
            file.write(content)

    def copy(self, path, source, dest ):
        shutil.copy2(path, dest / path.relative_to(source) )

class ResourceParser(Parser):
    extensions = [ ".jpg", ".png", ".gif", ".css", ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)

