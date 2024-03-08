from pytube import YouTube
from sys import argv


# Function will download highest-quality YouTube stream to current folder.
# If an argument is passed on the command line, it will download that file,
# otherwise the user will be prompted for a link
def main():
    if len(argv) > 1:
        link = argv[1]
    else:
        link = input("Enter a YouTube URL: ")

    yt = YouTube(link)
    print(f"Starting download of {yt.title}")
    yd = yt.streams.get_highest_resolution()

    yd.download()
    print("Download Complete")


if __name__ == "__main__":
    main()
