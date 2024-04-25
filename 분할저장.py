import tkinter as tk
from tkinter import filedialog
import os
from PIL import Image
def select_folder():
    root = tk.Tk()
    root.withdraw()  # tkinter 창 숨기기

    # 폴더 선택 대화상자 열기
    folder_path = filedialog.askdirectory()

    return folder_path

def get_image_paths(folder_path):
    image_paths = []
    # 폴더 내의 모든 파일들에 대해 반복
    for filename in os.listdir(folder_path):
        # 파일이 이미지 파일인지 확인
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # 이미지 파일의 절대 경로를 리스트에 추가
            image_paths.append(os.path.join(folder_path, filename))
    # 파일명에 포함된 숫자를 기준으로 정렬
    image_paths.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
    return image_paths

selected_folder = select_folder()
if selected_folder:
    image_paths = get_image_paths(selected_folder)



folder_path = filedialog.askdirectory()
# 폴더 내의 이미지 파일들의 절대 경로를 가져옴
last_lst=[]
# 이미지 파일들을 숫자 순서대로 잘라서 저장
for idx, image_path in enumerate(image_paths):
    img = Image.open(image_path)
    width, height = img.size

    # 이미지를 1000px 단위로 잘라서 저장
    for i in range(0, height, 1000):
        top = i
        bottom = min(i + 1000, height)
        cropped_img = img.crop((0, top, width, bottom))

        last_lst.append(cropped_img)
        # 새 파일명 지정
   

for i,li in enumerate(last_lst):
    save_path = os.path.join(folder_path, str(i)+'.jpg')

    li.save(save_path)

    print(f"이미지 저장: {save_path}")

# 사용 예시