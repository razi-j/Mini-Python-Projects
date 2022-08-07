from pytube import YouTube

def download(url):
    yt = YouTube(url)
    print("{}".format(yt.title))
    ch = str(input("Download as Mp4 (v) or as Audio (a)?: "))
    
    if ch.lower() == "a":
        filtered = yt.streams.filter(only_audio=True)
        streams = list(enumerate(filtered))
        for i in streams:
            print(i)
    elif ch.lower() == "v":
        filtered = yt.streams.filter(file_extension="mp4", only_video=True)
        streams = list(enumerate(filtered))
        for i in streams:
            print(i)
    else: print("Invalid Input")

if __name__ == "__main__":
    link = str(input("YT Video Link: "))
    download(link)
