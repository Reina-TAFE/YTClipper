#!../.venv/Scripts/python.exe
import yt_dlp
from static_ffmpeg import run
import subprocess
import os
import time
from file_handler import move_video, delete_file


class VideoManager:

    @staticmethod
    def download_video(url, title=None):
        ydl_opts = {
            'format_sort': ['res:1080', 'ext:mp4:m4a'],
            'merge_output_format': 'mp4',
            # Name format: Uploader - Title (ID).extension
            'outtmpl': f'{title if title is not None else "%(id)s"}.mp4',
        }

        try:
            print("Fetching and downloading video...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                ydl.download([url])
                filename = ydl.prepare_filename(info)
            print(f"Download complete! Saved as: {filename}")
            return filename
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod


    @staticmethod
    def clip_video( url, start_timestamp, end_timestamp, title, output_path):
        # temp_filename = f"{title}_copy.mp4"
        filename = VideoManager.download_video(url)
        print(filename)
        time.sleep(1)
        while not os.path.exists(filename):
            print(f"File {filename} does not exist!")
        if os.path.exists(filename):
            print(f"File {filename} exists!")
            input_video = f"./{filename}"
            output_video = f"{title}.mp4"
            start_time = start_timestamp
            print(start_time)
            end_time = end_timestamp
            print(end_time)
            command = [
             "static_ffmpeg",
             '-ss', f"{start_time}",  # Start time
             '-to', f"{end_time}",  # End time
             '-i', input_video,  # Input file (placed after -ss for faster seeking)
             '-c', 'copy',  # Copy video/audio streams directly without re-encoding
             output_video
            ]

            try:
                # subprocess.run(command, check=True, capture_output=True, text=True)
                command_str = " ".join(command)
                os.system(command_str)
                print(f"Successfully clipped video: {title}.mp4")
                if move_video(output_video, output_path):
                    print("Clipped successfully downloaded!")
                    delete_file(filename)
                else:
                    print("Failed to clip video!")
            except subprocess.CalledProcessError as e:
                print(f"ffmpeg Error: {e.stderr}")
        else:
            print(f"File not found: {filename}")