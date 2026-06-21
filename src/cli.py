
import os

import click
try:
    from video_manager import VideoManager
    from file_handler import delete
except:
    from  src.video_manager import VideoManager


@click.group()
def cli():
    pass

@cli.command()
@click.option('--url', '-u', default="https://youtu.be/X8avbciUP3c")
@click.option('--title', '-t', default="myVideo")
# @click.option('--output', "-o", default=None)
def download(url, title):
    try:
        if title is None:
            VideoManager.download_video(url)
        else:
            VideoManager.download_video(url, title)
    except Exception as e:
        print(e)

@cli.command()
@click.option('--url', '-u', default="https://youtu.be/X8avbciUP3c")
@click.option('--start', '-s', default="00:00:00")
@click.option('--end', '-e', default="00:00:05")
@click.option('--title', '-t', default="myclip")
@click.option('--output', '-o', default="./clips/")
def clip(url, start, end, title, output):
    try:
        VideoManager.clip_video(url, start, end, title, output)
    except Exception as e:
        print(e)

@cli.command()
@click.option('--path', "-p", default=None)
def delete_file(path):
    try:
        delete(path)
    except Exception as e:
        print(e)

@cli.command()
def version():
    print("Version 0.2")

if __name__ == '__main__':
    cli()