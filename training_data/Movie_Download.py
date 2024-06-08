import pytube

def download_highest_quality_video(url):
    # 유튜브 객체 생성
    youtube = pytube.YouTube(url)

    # 해상도 설정
    video_stream = youtube.streams.filter(res="360p").first()

    # 영상 다운로드
    video_stream.download()

    print('Video downloaded successfully!')

# 다운로드 받을 영상 링크 입력 
video_url = 'https://youtu.be/DiGkgTF45AE' 

download_highest_quality_video(video_url)

