import os

# 현재 디렉토리 내 모든 파일 목록 가져오기
file_list = os.listdir()

# mp4 파일에 대해서만 작업 수행
for file_name in file_list:
    if file_name.endswith('.mp4'):
        # mp4 파일명과 동일한 텍스트 파일명 생성
        text_file_name = file_name.replace('.mp4', '.txt')
        
        # 텍스트 파일 생성 후 내용 작성
        with open(text_file_name, 'w') as text_file:
            text_file.write("face milling, face cutter, horizontal milling".format(file_name))

print("텍스트 파일 생성이 완료되었습니다.")
