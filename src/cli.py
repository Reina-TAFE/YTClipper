#!../.venv/Scripts/python.exe
import os

import click
try:
    from video_manager import VideoManager
except:
    from  src.video_manager import VideoManager


@click.group()
def cli():
    pass

@cli.command()
@click.option('--url', "-u", default=None)
# @click.option('--title', "-t", default=None)
# @click.option('--output', "-o", default=None)
def download(url):
    try:
        VideoManager.download_video(url)
    except Exception as e:
        print(e)

@cli.command()
@click.option('--url')
@click.option('--start')
@click.option('--end')
@click.option('--title')
@click.option('--output')
def clip(url, start, end, title, output):
    try:
        VideoManager.clip_video(url, start, end, title, output)
    except Exception as e:
        print(e)

@cli.command()
@click.option('--path', "-p", default=None)
def delete_file(path):
    try:
        os.remove(path)
    except Exception as e:
        print(e)

@cli.command()
def version():
    print("Version 1.0")

if __name__ == '__main__':
    cli()