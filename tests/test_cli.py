from typer.testing import CliRunner

from weather.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, [77077])
    assert '77077' in result.stdout