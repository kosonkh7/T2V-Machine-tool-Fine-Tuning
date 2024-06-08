from moviepy.editor import VideoFileClip

def extract_samples(video_path, start_time, end_time):
    # 비디오 클립 객체 생성
    video_clip = VideoFileClip(video_path)
    
    # 추출할 샘플 영상 리스트 초기화
    sample_clips = []
    
    # 시작 시각부터 끝 시각까지 4초 단위로 반복하여 샘플 추출
    current_time = start_time
    while current_time <= end_time:
        # 샘플 영상을 추출하여 리스트에 추가
        sample_clip = video_clip.subclip(current_time, current_time + 4)
        sample_clips.append(sample_clip)
        
        # 다음 샘플을 위해 현재 시각을 4초 뒤로 이동
        current_time += 4
    
    return sample_clips

# 동영상 파일 경로 설정 
video_path = 'Chinese 50mm face mill.mp4'

# 추출할 샘플의 시작 시각과 끝 시각 설정 (예: 0초에서 60초 사이의 샘플)
start_time = 4
end_time = 34

# 샘플 영상 추출
samples = extract_samples(video_path, start_time, end_time)

# 자른 동영상 파일명 설정
output='Chinese 50mm face mill'

# 추출된 샘플 영상을 저장할 파일명 설정
for i, sample in enumerate(samples):
    sample_filename = f'{output}_{i}.mp4'
    sample.write_videofile(sample_filename)