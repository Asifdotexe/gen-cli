import sys

from gen.commands import helper, list_


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("--list", "list"):
            list_.list_langtemplates()
        elif sys.argv[1] in ["-h", "--help", "help"]:
            helper.help()
    else:
        pass
