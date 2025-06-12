from tree_sitter import Language, Parser
import tree_sitter_python
import tree_sitter_javascript
import tree_sitter_typescript
import tree_sitter_go
from pathlib import Path

# Registry with manually installed grammar bindings
LANGUAGE_REGISTRY = {
    "python": {
        "extensions": [".py"],
        "language": Language(tree_sitter_python.language())
    },
    "javascript": {
        "extensions": [".js", ".jsx"],
        "language": Language(tree_sitter_javascript.language())
    },
    "typescript": {
        "extensions": [".ts", ".tsx"],
        "language": Language(tree_sitter_typescript.language_typescript())
    },
    "tsx": {
        "extensions": [".tsx"],
        "language": Language(tree_sitter_typescript.language_tsx())
    },
    "go": {
        "extensions": [".go"],
        "language": Language(tree_sitter_go.language())
    }
}

def detect_language(file_path):
    ext = Path(file_path).suffix
    for lang, data in LANGUAGE_REGISTRY.items():
        if ext in data["extensions"]:
            return lang
    return None

def parse_code(file_path):
    lang_key = detect_language(file_path)
    if not lang_key:
        print(f"[SKIP] Unsupported file type: {file_path}")
        return

    lang_obj = LANGUAGE_REGISTRY[lang_key]["language"]
    parser = Parser(lang_obj)


    code = Path(file_path).read_text(encoding='utf-8', errors='ignore')
    tree = parser.parse(code.encode("utf-8"))
    root = tree.root_node

    print(f"[{lang_key.upper()}] File: {file_path}")
    print(f"Root node: {root.type}")
    print("Top-level children:")
    for child in root.children[:5]:
        print(f"  - {child.type} ({child.start_point} → {child.end_point})")
    print("-" * 40)

if __name__ == "__main__":
    # Create sample code files
    Path("sample.py").write_text("def hello():\n    print('Hello World')\n")
    Path("sample.js").write_text("function greet() { console.log('Hi'); }")
    Path("sample.ts").write_text("function add(a: number, b: number): number { return a + b; }")
    Path("sample.go").write_text("package main\nfunc main() { println(\"Hello\") }")

    for fname in ["sample.py", "sample.js", "sample.ts", "sample.go"]:
        parse_code(fname)
