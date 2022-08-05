from pytube import Youtube

def download(url):
    yt = Youtube(url)
    streamType = input("Download as Video or Audio (a/v)?: ")
    if streamType.lower() != "a" or streamType.lower() != "v":
        print("Invalid Input!")
    else:
        if streamType.lower() == "a":
            streams = yt.streams.filter(only_audio=True)
            selection = list(enumerate(streams))
            for i in selection:
                print(i)
        else:
            streams = yt.streams.filter(file_extension="mp4")
            selection = list(enumerate(streams))
            for i in selection:
                print(i)


if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=dQw4w9WgXcQ")