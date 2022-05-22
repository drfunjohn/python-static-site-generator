from os import wait
from pathlib import Path

class Site:

    def __init__(self, source, dest, parsers = None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers or []

    def create_dir(self, path):
        """
        create directory

        result: new directory path(relative to self.source) in the self.dest
        """
        directory = Path(self.dest /
                path.relative_to(self.source))
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        """
        build each dir from source in the dest
        """
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(self, extention):
        """
        load parser
        """
        for parser in self.parsers:
            if parser.valide_extention(extention):
                return parser

    def run_parser(self, path):
        """
        run parser
        """
        parser=self.load_parser(path.suffix)
        if parser is not None:
            parser.parse(path, self.source, self.dest)
        else:
            print("Not Implemented")
        
