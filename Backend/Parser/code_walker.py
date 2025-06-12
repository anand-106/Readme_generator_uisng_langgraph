import os
from pathlib import Path
from pprint import pprint

# Supported language extensions
SUPPORTED_EXTENSIONS = {
    ".py": "python",
    ".js":"javascript"
}

# Directories to exclude
EXCLUDED_DIRS = {".git", ".venv", "__pycache__", "node_modules", "dist", "build", ".mypy_cache"}

def walk_codebase(root_dir):

    code_files = []  #to store the file and path that needs to be parsed

    for dirpath,dirnames,filenames in os.walk(root_dir): #os.walk returns a tuple of dir path, dir name and file name

        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDED_DIRS]

        for file in filenames:

            if file.startswith('.'):
                continue

            filepath = Path(dirpath) / file #combines path with file name
            ext = filepath.suffix


            if ext in SUPPORTED_EXTENSIONS:
                code_files.append({
                    'path':filepath,
                    'language': SUPPORTED_EXTENSIONS[ext]
                })

    return code_files