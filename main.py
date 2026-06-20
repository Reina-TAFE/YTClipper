#!./.venv/Scripts/python.exe
try:
    from cli import cli
except ModuleNotFoundError:
    from src.cli import cli

if __name__ == "__main__":
    cli()