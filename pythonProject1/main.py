import time
from pytube import YouTube
import os, sys


def animation():
    print("Loading:")

    animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]",
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    print("\n")


def mainF():
    yt = YouTube(str(input("Enter link address: ")))

    video = yt.streams.filter(only_audio=True).first()

    animation()

    print("Enter the destination (leave blank for current directory)")
    destination = '.'

    mp4_file = video.download(output_path=destination)

    base, ext = os.path.splitext(mp4_file)
    new_file = base + '.mp3'
    os.rename(mp4_file, new_file)

    animation()

    print("Successfully downloaded " + yt.title)


if __name__ == "__main__":
    mainF()