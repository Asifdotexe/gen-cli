import unittest
import os
import sys
from unittest.mock import patch


class TestCLI(unittest.TestCase):
    def test_cli_module_exists(self):
        from gen import cli

        self.assertTrue(hasattr(cli, "main"))

    def test_handle_filename_requires_extension(self):
        from gen.cli import handle_filename

        with self.assertRaises(Exception):
            handle_filename("noextension")

    def test_parse_command_mode_help(self):
        from gen.cli import parse_command_mode
        import io
        from contextlib import redirect_stdout

        f = io.StringIO()
        with patch("sys.argv", ["gen", "--help"]):
            with redirect_stdout(f):
                try:
                    parse_command_mode()
                except SystemExit:
                    pass


class TestDoctor(unittest.TestCase):
    def test_doctor_module_exists(self):
        from gen.commands import doctor

        self.assertTrue(hasattr(doctor, "run_doctor"))

    def test_doctor_runs_without_error(self):
        from gen.commands import doctor

        doctor.run_doctor()


class TestConfig(unittest.TestCase):
    def test_extension_map_exists(self):
        from gen.config import EXTENSION_MAP

        self.assertIsInstance(EXTENSION_MAP, dict)

    def test_extension_map_has_common_extensions(self):
        from gen.config import EXTENSION_MAP

        self.assertIn(".py", EXTENSION_MAP)


class TestTemplate(unittest.TestCase):
    def test_template_module_exists(self):
        from gen.commands import template

        self.assertTrue(hasattr(template, "gen_langtemplate"))

    def test_list_module_exists(self):
        from gen.commands import list_

        self.assertTrue(hasattr(list_, "list_langtemplates"))


class TestCore(unittest.TestCase):
    def test_render_module_exists(self):
        from gen.core import render

        self.assertTrue(hasattr(render, "render_framework"))


if __name__ == "__main__":
    unittest.main()
