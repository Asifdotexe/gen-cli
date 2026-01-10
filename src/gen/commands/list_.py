EXTENSION_MAP = {
    ".py": "python",
    ".go": "go",
    ".c": "c",
    ".cpp": "cpp",
    ".js": "javascript",
    ".java": "java",
    ".rs": "rust",
    ".html": "html",
}


# import argparse


# Prints the Language Templetes
def list_langtemplates():
    for ext, lang in EXTENSION_MAP.items():
        print(lang)
