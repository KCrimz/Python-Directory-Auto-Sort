# organize the desktop
# moves images, videos, screenshots, and audio files
# into corresponding folders
import os
import shutil

#import necessary libraries for OS reading and moving
import os
import shutil

# defining file types for sorting using "dest_file extensions" I have some set here but feel free to add or change them
dest_audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

dest_videos = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
               ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")

dest_images = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd",
               ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt",
               ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")

dest_exe = ".exe"

dest_txt = ".txt"

dest_zip = ".zip"

# define functions to get each file type extension by using the index value.
def is_audio(file):
    return os.path.splitext(file)[1] in dest_audio


def is_video(file):
    return os.path.splitext(file)[1] in dest_videos


def is_image(file):
    return os.path.splitext(file)[1] in dest_images


def is_txt(file):
    return os.path.splitext(file)[1] in dest_txt


def is_exe(file):
    return os.path.splitext(file)[1] in dest_exe

def is_zip(file):
    return os.path.splitext(file)[1] in dest_zip

# choose directory to sort ex. /Users/Bob/Downloads this will sort everything in that directory
os.chdir("Directory Path here")

# Path sorting for each file type in the directory. This will refer to the previous defined function and cross compare
# the values to determine the extension and sort them into custom directories or other directories of your choosing
for file in os.listdir():
    if os.path.isdir(file):
        continue
    elif is_audio(file):
        shutil.move(file,"Audio directory Here")
    elif is_video(file):
        shutil.move(file,"Video directory Here")
    elif is_image(file):
        shutil.move(file,"Image directory Here")
    elif is_txt(file):
        shutil.move(file,"Txt directory Here" )
    elif is_exe(file):
        shutil.move(file,"Exe/program directory Here")
    elif is_zip(file):
        shutil.move(file,"Zip directory Here")
# this last else: statment is to sort anything remaining you havent defined into another directory. OR if you dont wish
# to move them just simply omit this part of the code as I have below. Otherwise delete the "#"
#   else:
#       shutil.move(file,"All other file type Directory Here")



