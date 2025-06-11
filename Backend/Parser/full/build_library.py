from tree_sitter import Language
import os

LANGUAGE_DIR = 'parsers'
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

language_paths = [os.path.join(LANGUAGE_DIR, repo) for repo in LANGUAGE_REPOS.values()]

# Make sure tree-sitter CLI isn't too new (optional, if you built this manually)
Language.build_library(
    BUILD_PATH,
    language_paths
)
print("✅ Successfully rebuilt shared library")
