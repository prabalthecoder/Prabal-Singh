from pytube import YouTube

def main():
    try:
        video_url    = input("Enter the youtube video URL (starting from www.youtube.com/).... : ")
        video_object = YouTube(video_url)

        destination = input("Where you want to save the file: ")

        pytube_object = video_object.streams.filter(type='video',
                                                    mime_type='video/mp4',
                                                    progressive=True).order_by('resolution').desc()[0]

        pytube_object.download(destination)
        print("Video: " + pytube_object.title + " downloaded successfully.")

    except Exception as e:
        print("Error occurred: {0}".format(repr(e)))

if __name__ == "__main__":
    main()
