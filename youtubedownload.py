import pytube

url = input('Enter url:') 
youtube = pytube.YouTube(url)
streams = youtube.streams.filter(progressive=True, file_extension='mp4') #.all()
for i in streams: print(i)

itag = int(input('Enter Itag For Download:'))
video = youtube.streams.get_by_itag(itag)
video.download('D:\Downloads\Video\Youtube Downloads')
print('Download Completed')

