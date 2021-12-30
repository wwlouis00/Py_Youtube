from pytube import YouTube

myVideo = YouTube("https://www.youtube.com/watch?v=fFNvWXUwbAU")
print("\n")
print("********Title************")

print("Video Title: "+myVideo.title)

print("\n")
print("********Thumbnail image************")
print(myVideo.thumbnail_url)
print("\n")
print("********Video Streams************")
print(myVideo.streams.all)
print("\n")
print("********Download video************")
print("********Wait Unit download is finished************")
myVideo.streams.first().download()
print("video is finished")