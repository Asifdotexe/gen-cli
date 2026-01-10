import sys

from gen.commands import helper, list_, template


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("--list", "list"):
            list_.list_langtemplates()
        elif sys.argv[1] in ["-h", "--help", "help"]:
            helper.help()
        elif "." in sys.argv[1]:
            filename, extension = sys.argv[1].split(".")
            if sys.argv[2]:
                template.gen_langtemplate(filename, "." + extension, flag=sys.argv[2])
            else:
                template.gen_langtemplate(filename, "." + extension)
    else:
        helper.help()
