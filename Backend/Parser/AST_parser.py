from parser_setup import get_parser,build_language_library
from pathlib import Path
import pprint

#parses a code file to return a parse tree
def parse_code_file(file_path: str,language: str):

    build_language_library()

    parser = get_parser(language)

    code = Path(file_path).read_text(encoding="utf-8")

    tree = parser.parse(bytes(code,'utf8'))

    return tree

pprint(parse_code_file(file_path='Backend/Parser/code_walker.py',language='python'))