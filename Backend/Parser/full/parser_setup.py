from tree_sitter import Language, Parser
import os

LANGUAGE_DIR = 'Parser/parsers'
BUILD_PATH = 'build/my-languages.so'

LANGUAGE_REPOS = {
    "python": "tree-sitter-python",
    "javascript": "tree-sitter-javascript",
    "typescript": "tree-sitter-typescript/typescript",
    "java": "tree-sitter-java",
    "go": "tree-sitter-go",
    "cpp": "tree-sitter-cpp",
    "c": "tree-sitter-c"
}

def build_language_library():
    language_paths = [os.path.join(LANGUAGE_DIR, repo) for repo in LANGUAGE_REPOS.values()]
    Language.build_library(
        BUILD_PATH,
        language_paths
    )
    print(f"✅ Built shared library at {BUILD_PATH}")

# ✅ Correct usage with tree_sitter==0.20.1
LANGUAGE_MAPPING = {
    lang: Language(BUILD_PATH, lang)
    for lang in LANGUAGE_REPOS.keys()
}

def get_parser(language_name):
    if language_name not in LANGUAGE_MAPPING:
        raise ValueError(f"Unsupported language: {language_name}")
    parser = Parser()
    parser.set_language(LANGUAGE_MAPPING[language_name])
    return parser
