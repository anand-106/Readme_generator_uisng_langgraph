from tree_sitter import Language,Parser
import os

LANGUAGE_DIR = 'Backend/Parser/parsers'

BUILD_PATH = 'Backend/build/my-languages.so'

LANGUAGE_REPOS = {
    "python": "tree-sitter-python",
    "javascript": "tree-sitter-javascript",
    "typescript": "tree-sitter-typescript/typescript",
    "tsx": "tree-sitter-typescript/tsx",
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
    print(f"Built shared library at {BUILD_PATH}")



# Mapping from language name to compiled Language object
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

if __name__ == "__main__":
    if not os.path.exists(BUILD_PATH):
        build_language_library()
    else:
        print("✅ Shared library already built.")