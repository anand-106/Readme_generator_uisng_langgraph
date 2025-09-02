from tree_sitter import Language, Parser
from pathlib import Path
import tree_sitter_typescript as tsts


def extract_symbols_from_ts_file(file_path):
    TS_LANGUAGE = Language(tsts.language_typescript())
    parser = Parser(TS_LANGUAGE)
    try:
        code = Path(file_path).read_text(encoding="utf-8")
    except:
        return [], {"external": [], "internal": []}

    tree = parser.parse(code.encode("utf-8"))
    root = tree.root_node
    symbols = []
    imports = {"external": [], "internal": []}

    def extract_raw_code(node, code_str):
        return code_str[node.start_byte:node.end_byte]

    def extract_function_calls(node, code_str):
        calls = []

        def walk(n):
            if n.type == "call_expression":
                func = n.child_by_field_name("function")
                if func:
                    calls.append(code_str[func.start_byte:func.end_byte])
            for child in n.children:
                walk(child)

        walk(node)
        return calls

    def extract_parameters(node, code_str):
        params_node = node.child_by_field_name("parameters")
        if params_node:
            return [
                code_str[c.start_byte:c.end_byte]
                for c in params_node.children
                if c.type != "," and c.type != ")"
            ]
        return []

    def calculate_complexity(node):
        complexity = 1

        def walk(n):
            nonlocal complexity
            if n.type in ("if_statement", "for_statement", "while_statement", "switch_statement", "try_statement"):
                complexity += 1
            for child in n.children:
                walk(child)

        walk(node)
        return complexity

    def walk(node, parent=None):
        nonlocal code

        if node.type == "import_declaration":
            module_node = node.child_by_field_name("source")
            if module_node:
                name = code[module_node.start_byte:module_node.end_byte].strip("\"'")
                if name.startswith("."):
                    imports["internal"].append(name)
                else:
                    imports["external"].append(name)

        if node.type in ("class_declaration", "interface_declaration"):
            name_node = node.child_by_field_name("name")
            if name_node:
                name = code[name_node.start_byte:name_node.end_byte]
                symbols.append({
                    "type": "class" if node.type == "class_declaration" else "interface",
                    "name": name,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1,
                    "lines": node.end_point[0] - node.start_point[0] + 1,
                    "parameters": [],
                    "calls": extract_function_calls(node, code),
                    "complexity": calculate_complexity(node),
                    "docstring": None,
                    "raw_code": extract_raw_code(node, code),
                    "chunk_id": f"{Path(file_path).name}::{name}",
                    "decorators": []
                })

        if node.type in ("function_declaration", "arrow_function", "function_expression", "method_definition"):
            name_node = node.child_by_field_name("name")
            if not name_node and parent:
                if parent.type == "variable_declarator":
                    name_node = parent.child_by_field_name("name")
            name = code[name_node.start_byte:name_node.end_byte] if name_node else "<anonymous>"

            symbols.append({
                "type": "function",
                "name": name,
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "lines": node.end_point[0] - node.start_point[0] + 1,
                "parameters": extract_parameters(node, code),
                "calls": extract_function_calls(node, code),
                "complexity": calculate_complexity(node),
                "docstring": None,
                "raw_code": extract_raw_code(node, code),
                "chunk_id": f"{Path(file_path).name}::{name}",
                "decorators": []
            })

        for child in node.children:
            walk(child, node)

    walk(root)
    return symbols, imports


def extract_symbols_from_tsx_file(file_path):
    TSX_LANGUAGE = Language(tsts.language_tsx())
    parser = Parser(TSX_LANGUAGE)
    try:
        code = Path(file_path).read_text(encoding="utf-8")
    except:
        return [], {"external": [], "internal": []}

    tree = parser.parse(code.encode("utf-8"))
    root = tree.root_node
    symbols = []
    imports = {"external": [], "internal": []}

    def extract_raw_code(node, code_str):
        return code_str[node.start_byte:node.end_byte]

    def extract_function_calls(node, code_str):
        calls = []

        def walk(n):
            if n.type == "call_expression":
                func = n.child_by_field_name("function")
                if func:
                    calls.append(code_str[func.start_byte:func.end_byte])
            for child in n.children:
                walk(child)

        walk(node)
        return calls

    def extract_parameters(node, code_str):
        params_node = node.child_by_field_name("parameters")
        if params_node:
            return [
                code_str[c.start_byte:c.end_byte]
                for c in params_node.children
                if c.type != "," and c.type != ")"
            ]
        return []

    def calculate_complexity(node):
        complexity = 1

        def walk(n):
            nonlocal complexity
            if n.type in ("if_statement", "for_statement", "while_statement", "switch_statement", "try_statement"):
                complexity += 1
            for child in n.children:
                walk(child)

        walk(node)
        return complexity

    def walk(node, parent=None):
        nonlocal code

        if node.type == "import_declaration":
            module_node = node.child_by_field_name("source")
            if module_node:
                name = code[module_node.start_byte:module_node.end_byte].strip("\"'")
                if name.startswith("."):
                    imports["internal"].append(name)
                else:
                    imports["external"].append(name)

        if node.type in ("class_declaration", "interface_declaration"):
            name_node = node.child_by_field_name("name")
            if name_node:
                name = code[name_node.start_byte:name_node.end_byte]
                symbols.append({
                    "type": "class" if node.type == "class_declaration" else "interface",
                    "name": name,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1,
                    "lines": node.end_point[0] - node.start_point[0] + 1,
                    "parameters": [],
                    "calls": extract_function_calls(node, code),
                    "complexity": calculate_complexity(node),
                    "docstring": None,
                    "raw_code": extract_raw_code(node, code),
                    "chunk_id": f"{Path(file_path).name}::{name}",
                    "decorators": []
                })

        if node.type in ("function_declaration", "arrow_function", "function_expression", "method_definition"):
            name_node = node.child_by_field_name("name")
            if not name_node and parent:
                if parent.type == "variable_declarator":
                    name_node = parent.child_by_field_name("name")
            name = code[name_node.start_byte:name_node.end_byte] if name_node else "<anonymous>"

            symbols.append({
                "type": "function",
                "name": name,
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "lines": node.end_point[0] - node.start_point[0] + 1,
                "parameters": extract_parameters(node, code),
                "calls": extract_function_calls(node, code),
                "complexity": calculate_complexity(node),
                "docstring": None,
                "raw_code": extract_raw_code(node, code),
                "chunk_id": f"{Path(file_path).name}::{name}",
                "decorators": []
            })

        for child in node.children:
            walk(child, node)

    walk(root)
    return symbols, imports


