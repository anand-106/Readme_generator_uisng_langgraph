import os
from pathlib import Path
from pprint import pprint

# Supported language extensions
SUPPORTED_EXTENSIONS = {
    # ==== Code ====
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".java": "java",
    ".c": "c",
    ".cpp": "cpp",
    ".cc": "cpp",
    ".cxx": "cpp",
    ".h": "c",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".rb": "ruby",
    ".go": "go",
    ".rs": "rust",
    ".php": "php",
    ".swift": "swift",
    ".kt": "kotlin",
    ".kts": "kotlin",
    ".dart": "dart",
    ".scala": "scala",
    ".sh": "bash",
    ".bash": "bash",
    ".zsh": "bash",
    ".ps1": "powershell",
    ".lua": "lua",
    ".r": "r",
    ".jl": "julia",

    # ==== Web ====
    ".html": "html",
    ".htm": "html",
    ".css": "css",
    ".scss": "scss",
    ".sass": "sass",
    ".less": "less",

    # ==== Data / Config ====
    ".json": "json",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".xml": "xml",
    ".toml": "toml",
    ".ini": "ini",
    ".cfg": "ini",
    ".conf": "config",
    ".csv": "csv",
    ".tsv": "tsv",
    ".parquet": "parquet",
    ".sql": "sql",

    # ==== Docs / Text ====
    ".md": "markdown",
    ".rst": "restructuredtext",
    ".txt": "text",
    ".log": "log",

    # ==== Build / Package / Meta ====
    "Dockerfile": "dockerfile",
    "Makefile": "makefile",
    "CMakeLists.txt": "cmake",
    "package.json": "node",
    "package-lock.json": "node",
    "requirements.txt": "pip",
    "Pipfile": "pipenv",
    "pyproject.toml": "poetry",
    "setup.py": "setuptools",
    "build.gradle": "gradle",
    "pom.xml": "maven",

    # ==== CI/CD / VCS ====
    ".env": "env",
    ".editorconfig": "config",
    ".gitignore": "gitignore",
    ".gitattributes": "git",
    ".gitmodules": "git",
    ".travis.yml": "travis",
    ".prettierrc": "config",
    ".eslintrc": "config",
    ".babelrc": "config",
    ".npmrc": "config",

    # ==== Images ====
    ".jpg": "image",
    ".jpeg": "image",
    ".png": "image",
    ".gif": "image",
    ".svg": "image",
    ".bmp": "image",
    ".webp": "image",
    ".ico": "image",
    ".tiff": "image",
    ".psd": "image",
    ".heic": "image",

    # ==== Audio ====
    ".mp3": "audio",
    ".wav": "audio",
    ".ogg": "audio",
    ".flac": "audio",
    ".aac": "audio",
    ".m4a": "audio",
    ".wma": "audio",

    # ==== Video ====
    ".mp4": "video",
    ".mkv": "video",
    ".webm": "video",
    ".avi": "video",
    ".mov": "video",
    ".wmv": "video",
    ".flv": "video",
    ".m4v": "video",

    # ==== Archives ====
    ".zip": "archive",
    ".tar": "archive",
    ".gz": "archive",
    ".rar": "archive",
    ".7z": "archive",

    # ==== Fonts ====
    ".ttf": "font",
    ".otf": "font",
    ".woff": "font",
    ".woff2": "font",
}


# Directories to exclude
EXCLUDED_DIRS = {".git", ".venv", "__pycache__", "node_modules", "dist","public", "build", ".mypy_cache"}

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

def walk_full_codebase(root_dir):

    code_files = []  

    for dirpath,dirnames,filenames in os.walk(root_dir): #os.walk returns a tuple of dir path, dir name and file name

        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDED_DIRS]

        for file in filenames:

            if file.startswith('.'):
                continue

            filepath = Path(dirpath) / file 
            ext = filepath.suffix


            if ext in SUPPORTED_EXTENSIONS:
                code_files.append({
                    'path':filepath,
                    'language': SUPPORTED_EXTENSIONS[ext]
                })

    return code_files