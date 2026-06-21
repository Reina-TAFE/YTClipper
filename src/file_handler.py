import os
import shutil

def move_video(filename, destination):
    if os.path.exists(filename):
        if not os.path.exists(destination):
            os.makedirs(destination, exist_ok=True)
        try:
            new_location = shutil.move(filename, destination)
            print(f"file successfully moved to: {new_location}")
            return True
        except Exception as e:
            print(e)
            return False
    else:
        print(f"file does not exist: {filename}")

def delete(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            if not os.path.exists(path):
                print(f"Successfully deleted {path}!")
                return True
    except Exception as e:
        print(f"Could Not Delete: {e}")