#!/usr/bin/env python3
try:
    from cli import cli
except:
    from src.cli import cli

if __name__ == "__main__":
    cli()