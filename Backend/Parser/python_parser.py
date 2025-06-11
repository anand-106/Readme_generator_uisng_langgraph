import tree_sitter_python as tspython
from tree_sitter import Language, Parser
from pathlib import Path
from code_walker import walk_codebase
import pprint

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

def extract_symbols_from_file(file_path):
    code = Path(file_path).read_text(encoding='utf-8')
    tree = parser.parse(code.encode("utf8"))
    root = tree.root_node

    symbols = []

    def walk(node):
        if node.type in ("function_definition", "class_definition"):
            name_node = node.child_by_field_name("name")
            symbol_name = code[name_node.start_byte:name_node.end_byte]
            symbols.append({
                "type": node.type.replace("_definition", ""),
                "name": symbol_name,
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "docstring": extract_docstring(node, code)
            })
        for child in node.children:
            walk(child)

    walk(root)
    return symbols

def extract_docstring(node, code: str):
    body = node.child_by_field_name("body")
    if not body or len(body.children) == 0:
        return None
    first_child = body.children[0]
    if first_child.type == "expression_statement":
        string_node = first_child.children[0]
        if string_node.type == "string":
            return code[string_node.start_byte:string_node.end_byte].strip("\"'")
    return None

def analyze_codebase(root_dir):
    files = walk_codebase(root_dir)
    result = {}

    for file in files:
        path = file["path"]
        lang = file["language"]

        if lang == "python":
            result[str(path)] = extract_symbols_from_file(path)

    return result

if __name__ == "__main__":
    from pprint import pprint
    result = analyze_codebase("C:/Users/gamin/Documents/projects/Langchain-new/")
    pprint(result)
