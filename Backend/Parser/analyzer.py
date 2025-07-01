import json
from pathlib import Path
from collections import defaultdict
import re

from .code_walker import walk_codebase
from .js_parser import extract_symbols_from_js_file as extract_js
from .python_parser import extract_symbols_from_file as extract_py

def analyze_codebase(root_dir):
    files = walk_codebase(root_dir)
    project_name =  Path(root_dir).name
    folder_map = defaultdict(list)

    total_functions= 0
    total_classes = 0
    languages_used = set()

    for file in files:
        file_path = file['path']
        language = file['language']
        rel_path = Path(file_path).relative_to(root_dir)
        folder = str(Path(rel_path).parent).replace('\\','/')

        symbols = []

        if language == "python":
            symbols,_ = extract_py(file_path)
        elif language == "javascript":
            symbols,_ = extract_js(file_path)
        
        total_functions += sum(1 for s in symbols if s["type"] == "function")
        total_classes += sum(1 for s in symbols if s["type"] == "class")

        languages_used.add(language)

        folder_map[folder].append({
            "name": file_path.name,
            "language": language,
            "relative_path": str(rel_path),
            "symbols": symbols
        })
    
    print("successfully parsed files")

    return {
    "project": project_name,
    "metadata": {
        "total_files": len(files),
        "total_functions": total_functions,
        "total_classes": total_classes,
        "languages_used": list(languages_used)
    },
    "structure": [
        {
            "folder": folder,
            "files": files
        } for folder, files in folder_map.items()
    ]
    }
    

if __name__ == "__main__":
    # 🔧 Change this to your target project directory
    root = "C:/Users/gamin/Documents/Harkirat/Code_Class/day-9/todo-fe/src"
    result = analyze_codebase(root)

    print(type(result))

    output_file = f"{result['project']}_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Analysis saved to: {output_file}")
    print(f"📁 Total files analyzed: {result['metadata']['total_files']}")
    print(f"🔧 Total functions: {result['metadata']['total_functions']}")
    print(f"🏛️ Total classes: {result['metadata']['total_classes']}")
    print(f"💬 Languages used: {', '.join(result['metadata']['languages_used'])}")