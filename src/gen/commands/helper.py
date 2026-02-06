class colors:
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    ENDC = "\033[0m"


HELP_TEXT = """
Gen-CLI — Generate boilerplate files and framework project templates
for multiple programming languages.

USAGE:
    gen <command> [arguments]

COMMANDS:
    gen <file.ext>           Generate a single file from extension (e.g. main.py)
    gen new <name> --lang <lang> --template <template>  Create a project
    gen list                 List all available templates
    gen tree [path]          Show directory tree
    gen tree -r              Show tree recursively
    gen tree -d <n>          Show tree with depth n
    gen doctor               Check environment and configuration
    gen --version, -v        Show version
    gen --help, -h           Show this help

EXAMPLES:
    gen main.py                    # Generate Python file
    gen new myapp --lang python --template fastapi
    gen tree                       # Current directory tree
    gen tree -r                    # Recursive tree
    gen tree -d 2                  # Tree with depth 2
    gen doctor                     # Environment check
    gen --version                  # Show version

For more info on a command: gen <command> --help

Supported Languages: python, go, rust, c, cpp, java, javascript, html
"""


COMMANDS_TEXT = """
AVAILABLE COMMANDS:

    gen <filename.extension>
        Generate a single file (main.py, app.go, index.js, etc.)

    gen new <name> --lang <lang> --template <template>
        Generate a project from template

    gen list
        List all available templates

    gen tree [path]
        Show directory tree (default depth 1)

    gen tree -r [path]
        Show tree recursively (all levels)

    gen tree -d <n> [path]
        Show tree with depth n

    gen doctor
        Check environment and configuration

    gen --version, -v
        Show installed version

    gen --help, -h
        Show this help message
"""


def help():
    print(colors.GREEN + HELP_TEXT + colors.ENDC)


def concise_help():
    print(colors.GREEN + COMMANDS_TEXT + colors.ENDC)
