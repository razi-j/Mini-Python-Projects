from pytube import YouTube
import time

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
        filtered = yt.streams.filter(file_extension="mp4")
        streams = list(enumerate(filtered))
        for i in streams:
            print(i)
    else: print("Invalid Input")

    try:
        index = int(input("Enter the Index of the Format you want to download: "))
        filtered[index].download()
        print("Download Completed!")
    except:
        print("An Unexpected Error has Occured!!")
    

if __name__ == "__main__":
    while True:
        link = str(input("YT Video Link: "))
        download(link)
        restart = input("Download another video (y/n)?: ")
        if restart.lower() == "y":
            continue
        elif restart.lower() == "n":
            print("Goodbye!")
            time.sleep(3)
            quit()