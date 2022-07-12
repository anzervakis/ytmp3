from pytube import (YouTube,Playlist)

import datetime

print('--------------------YOUTUBE DOWNLOADER--------------------')

playlist_or_video=input('Playlist or Video: ')

if playlist_or_video=='video':
    
    input_field=input('Enter link: ')

    yt = YouTube(input_field)

    views = yt.views

    title = yt.title

    length = yt.length

    video_length = datetime.timedelta(seconds = length)

    print('Video Title:',title)
            
    print('Video Views:',views)
            
    print('Video Length:',video_length)
        
    download_file_video = yt.streams.filter(file_extension="mp4").get_highest_resolution()

    confirm=input('Download? y/n: ')
    
    if confirm=='y' or confirm=='Y':

        print('Downloading',title)

        download_file_video.download()
    
    elif confirm=='n' or confirm=='N':

        quit()

        
        

elif playlist_or_video=='playlist':
    
    input_field=input('Enter link: ')

    pl = Playlist(input_field)

    title_playlist=pl.title

    views_playlist=pl.views

    videos = len(pl.videos)

    video_list=pl.video_urls

    print('Playlist Length:',videos,'videos')
        
    videos_list_position=0

    confirm=input('Download? y/n: ')

    if confirm=='y' or confirm=='Y':   
        
        for i in range(videos):
                    
            video_for_download_get=video_list[videos_list_position]
                    
            video_for_download=YouTube(video_for_download_get)
                    
            video_download=video_for_download.streams.filter(file_extension="mp4").get_highest_resolution()
                    
            print(f'Downloading {video_download.title}')

            video_download.download()
                    
            videos_list_position=videos_list_position+1
    
    
    elif confirm=='n' or confirm=='N':
        
        quit()
        
