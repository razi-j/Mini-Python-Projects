from pytube import YouTube

rs = ["a", "v"]

def download(url):
    yt = YouTube(url)
    ch = str(input("Download as Mp4 (v) or as Audio (a)?: "))
    
    if ch.lower not in rs:
        print("Invalid Input")
    elif ch.lower() == "a":
        filtered = yt.streams.filter(only_audio=True)
        streams = list(enumerate(filtered))
        for i in streams:
            print(i)

if __name__ == "__main__":
    link = str(input("YT Video Link: "))
    download(link)
