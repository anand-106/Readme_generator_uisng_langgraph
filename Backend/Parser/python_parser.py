import os
import tree_sitter_python as tspython
import tree_sitter_javascript as tsjs
from tree_sitter import Language, Parser
from pathlib import Path
from Parser.code_walker import walk_codebase

import pprint
from collections import defaultdict
import re
import json

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

def extract_raw_code(node, code):
    """Extract the raw code for a symbol"""
    return code[node.start_byte:node.end_byte]

def extract_imports(root_node, code):
    """Extract import statements from the file"""
    imports = {"external": [], "internal": []}
    
    def walk_imports(node):
        if node.type == "import_statement":
            for child in node.children:
                if child.type == "dotted_name":
                    module_name = code[child.start_byte:child.end_byte]
                    if module_name.startswith('.') or '/' in module_name or '\\' in module_name:
                        imports["internal"].append(module_name)
                    else:
                        imports["external"].append(module_name)
        
        elif node.type == "import_from_statement":
            module_node = node.child_by_field_name("module_name")
            if module_node:
                module_name = code[module_node.start_byte:module_node.end_byte]
                if module_name.startswith('.'):
                    imports["internal"].append(module_name)
                else:
                    imports["external"].append(module_name)
        
        for child in node.children:
            walk_imports(child)
    
    walk_imports(root_node)
    return imports

def extract_function_calls(node, code):
    """Extract function calls within a symbol"""
    calls = []
    
    def walk_calls(node):
        if node.type == "call":
            func_node = node.child_by_field_name("function")
            if func_node:
                func_name = code[func_node.start_byte:func_node.end_byte]
                calls.append(func_name)
        
        for child in node.children:
            walk_calls(child)
    
    walk_calls(node)
    return calls

def extract_decorators(node, code):
    """Extract decorators for functions/classes"""
    decorators = []
    for child in node.children:
        if child.type == "decorator":
            decorator_text = code[child.start_byte:child.end_byte]
            decorators.append(decorator_text)
    return decorators

def extract_parameters(node, code):
    """Extract function parameters"""
    parameters = []
    params_node = node.child_by_field_name("parameters")
    if params_node:
        for child in params_node.children:
            if child.type == "identifier":
                param_name = code[child.start_byte:child.end_byte]
                parameters.append({"name": param_name, "type": None, "default": None})
    return parameters

def calculate_complexity(node):
    """Simple complexity calculation based on control flow"""
    complexity = 1  # Base complexity
    
    def count_complexity(node):
        nonlocal complexity
        if node.type in ("if_statement", "for_statement", "while_statement", 
                        "try_statement", "with_statement", "match_statement"):
            complexity += 1
        
        for child in node.children:
            count_complexity(child)
    
    count_complexity(node)
    return complexity

def detect_file_purpose(file_path, symbols, imports):
    """Heuristically determine the file's purpose"""
    file_name = file_path.name.lower()
    
    # API/Route files
    if any(imp in imports["external"] for imp in ["fastapi", "flask", "django"]):
        return "api_endpoint"
    
    # Database models
    if "model" in file_name or any(imp in imports["external"] for imp in ["sqlalchemy", "django.db", "mongoengine"]):
        return "data_model"
    
    # Main entry points
    if file_name in ["main.py", "app.py", "__init__.py"]:
        return "entry_point"
    
    # Authentication
    if "auth" in file_name:
        return "authentication"
    
    # Configuration
    if "config" in file_name or "settings" in file_name:
        return "configuration"
    
    # Test files
    if "test" in file_name:
        return "test"
    
    return "core_logic"

def extract_symbols_from_file(file_path):
    """Enhanced symbol extraction with full metadata"""
    try:
        code = Path(file_path).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        try:
            code = Path(file_path).read_text(encoding='latin-1')
        except:
            return [], {}
    
    tree = parser.parse(code.encode("utf8"))
    root = tree.root_node
    symbols = []
    
    # Extract file-level imports
    file_imports = extract_imports(root, code)
    
    def walk(node):
        if node.type in ("function_definition", "class_definition"):
            name_node = node.child_by_field_name("name")
            symbol_name = code[name_node.start_byte:name_node.end_byte]
            
            # Extract detailed information
            raw_code = extract_raw_code(node, code)
            docstring = extract_docstring(node, code)
            decorators = extract_decorators(node, code)
            function_calls = extract_function_calls(node, code)
            complexity = calculate_complexity(node)
            
            symbol_info = {
                "type": node.type.replace("_definition", ""),
                "name": symbol_name,
                "start_line": node.start_point[0] + 1,
                "end_line": node.end_point[0] + 1,
                "lines": node.end_point[0] - node.start_point[0] +1,
                "docstring": docstring,
                "raw_code": raw_code,
                "chunk_id": f"{file_path.name}::{symbol_name}",
                "decorators": decorators,
                "calls": function_calls,
                "complexity": complexity
            }
            
            # Add function-specific info
            if node.type == "function_definition":
                symbol_info["parameters"] = extract_parameters(node, code)
            
            symbols.append(symbol_info)
        
        for child in node.children:
            walk(child)
    
    walk(root)
    return symbols, file_imports

def analyze_codebase_with_folders(root_dir):
    """Enhanced codebase analysis with full metadata"""
    files = walk_codebase(root_dir)
    project_name = Path(root_dir).name
    folder_map = defaultdict(list)
    
    # Track global dependencies and API endpoints
    all_dependencies = {"external": set(), "internal": set()}
    api_endpoints = []
    
    for file in files:
        path = file["path"]
        lang = file["language"]
        
        if lang == "python":
            symbols, file_imports = extract_symbols_from_file(path)
            
            # Update global dependencies
            all_dependencies["external"].update(file_imports["external"])
            all_dependencies["internal"].update(file_imports["internal"])
            
            # Detect API endpoints
            for symbol in symbols:
                if symbol["decorators"]:
                    for decorator in symbol["decorators"]:
                        if any(method in decorator.lower() for method in ["@app.get", "@app.post", "@app.put", "@app.delete"]):
                            # Extract endpoint path from decorator
                            path_match = re.search(r'["\']([^"\']*)["\']', decorator)
                            if path_match:
                                api_endpoints.append({
                                    "path": path_match.group(1),
                                    "method": decorator.split('.')[1].split('(')[0].upper(),
                                    "function": symbol["name"],
                                    "file": path.name
                                })
            
            rel_path = Path(os.path.relpath(path, root_dir))
            folder = str(rel_path.parent).replace("\\", "/")
            
            # Detect file purpose
            file_purpose = detect_file_purpose(path, symbols, file_imports)
            
            folder_map[folder].append({
                "name": path.name,
                "relative_path": str(rel_path).replace("\\", "/"),
                "file_type": file_purpose,
                "purpose": generate_file_purpose_description(file_purpose, symbols),
                "imports": file_imports,
                "symbols": symbols
            })
    
    # Generate architecture overview
    architecture = analyze_architecture(folder_map, all_dependencies)
    
    return {
        "project": project_name,
        "metadata": {
            "total_files": len(files),
            "total_functions": sum(len([s for s in folder_files["symbols"] if s["type"] == "function"]) 
                                 for folder_data in folder_map.values() 
                                 for folder_files in folder_data),
            "total_classes": sum(len([s for s in folder_files["symbols"] if s["type"] == "class"]) 
                               for folder_data in folder_map.values() 
                               for folder_files in folder_data),
            "primary_language": "python"
        },
        "dependencies": {
            "external": list(all_dependencies["external"]),
            "internal": list(all_dependencies["internal"])
        },
        "api_endpoints": api_endpoints,
        "architecture": architecture,
        "structure": [
            {
                "folder": folder,
                "files": files
            }
            for folder, files in folder_map.items()
        ]
    }

def generate_file_purpose_description(file_type, symbols):
    """Generate human-readable purpose description"""
    purposes = {
        "api_endpoint": "REST API endpoints and route handlers",
        "data_model": "Database models and data structures", 
        "entry_point": "Application entry point and initialization",
        "authentication": "User authentication and authorization",
        "configuration": "Application configuration and settings",
        "test": "Unit tests and test utilities",
        "core_logic": "Core business logic and functionality"
    }
    return purposes.get(file_type, "Application logic")

def analyze_architecture(folder_map, dependencies):
    """Analyze and categorize the codebase architecture"""
    architecture = {
        "pattern": "unknown",
        "layers": {}
    }
    
    # Detect common patterns
    folders = list(folder_map.keys())
    
    if any("api" in folder.lower() or "routes" in folder.lower() for folder in folders):
        architecture["pattern"] = "layered_architecture"
    elif "models" in str(folders) and "views" in str(folders):
        architecture["pattern"] = "mvc"
    elif len(folders) > 3:
        architecture["pattern"] = "microservices"
    
    # Categorize layers
    for folder, files in folder_map.items():
        if any(f["file_type"] == "api_endpoint" for f in files):
            architecture["layers"]["api"] = architecture["layers"].get("api", []) + [folder]
        elif any(f["file_type"] == "data_model" for f in files):
            architecture["layers"]["data"] = architecture["layers"].get("data", []) + [folder]
        elif any(f["file_type"] == "authentication" for f in files):
            architecture["layers"]["auth"] = architecture["layers"].get("auth", []) + [folder]
    
    return architecture

def extract_docstring(node, code: str):
    """Enhanced docstring extraction"""
    body = node.child_by_field_name("body")
    if not body or len(body.children) == 0:
        return None
    
    first_child = body.children[0]
    if first_child.type == "expression_statement":
        string_node = first_child.children[0]
        if string_node.type == "string":
            docstring = code[string_node.start_byte:string_node.end_byte]
            # Clean up the docstring
            return docstring.strip("\"'").strip()
    
    return None

if __name__ == "__main__":
    result = analyze_codebase_with_folders("C:/Users/gamin/Documents/projects/Langchain-new/")
    output_file = f"{result['project']}_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"Analysis saved to: {output_file}")
    print(f"Total files analyzed: {result['metadata']['total_files']}")
    print(f"Total functions: {result['metadata']['total_functions']}")
    print(f"Total classes: {result['metadata']['total_classes']}")