from unittest import TestCase
from click.testing import CliRunner

from example_project.cli import cli


class TestCLI(TestCase):
    def setUp(self):
        self.runner: CliRunner = CliRunner()

    def test__cli_invoke(self):
        result = self.runner.invoke(cli)
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Usage", result.output)
