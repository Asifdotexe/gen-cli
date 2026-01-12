import sys

from gen.commands import helper, list_, template
from gen.config import EXTENSION_MAP


def main():
    if len(sys.argv) < 2:
        helper.help()
        return

    cmd = sys.argv[1]

    if cmd in ("--list", "list"):
        list_.list_langtemplates()
    elif cmd in ["-h", "--help", "help"]:
        helper.help()
    elif "." in cmd:
        try:
            parts = sys.argv[1].split(".")

            filename, extension = parts[0], "." + parts[1]

            flag = sys.argv[2] if len(sys.argv) > 2 else None

            if flag:
                template.gen_langtemplate(filename, extension, flag=flag)
            else:
                template.gen_langtemplate(filename, extension)
        except:
            print("gen <filename.extension>")

    # check wheather lang has templates
    elif sys.argv[1] == "new":
        try:
            if (
                "--" in sys.argv[3]
                and sys.argv[3] in EXTENSION_MAP.values()
                and "--" in sys.argv[4]
            ):
                dir_name, lang, framework = (
                    sys.argv[2],
                    sys.argv[3][2:],
                    sys.argv[4][2:],
                )
                template.gen_framtemplate(dir_name, lang, framework)
        except IndexError:
            print("gen new <dir name> <lang> <framework>")
    else:
        print("gen <filename.extension>")
