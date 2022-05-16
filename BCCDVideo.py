import os
import cv2
from glob import glob

#this program turns video frames into png images
#Resources:
#Wings Lectures: https://www.youtube.com/watch?v=42C38oCoYes
#Geeks for Geeks: https://www.geeksforgeeks.org/opencv-python-tutorial/
#Roboflow Detectron2: https://colab.research.google.com/drive/1JkBGyLQI_pkC0W2b9fNX9x4Dnn6RWgPh
#w3schools: https://www.w3schools.com/python/python_try_except.asp
#Idiot Developer: https://www.youtube.com/watch?v=SWGd2hX5p3U&t=448s

#method to save each frame while the video is playing
def save_frame(vid_folder, save_dir):
    label = vid_folder.split("/")[-1].split(".")[0]

    #each video will save its frames in their own file
    save_path = os.path.join(save_dir, label)
    new_dir(save_path)

    scene = cv2.VideoCapture(vid_folder)
    count = 0

    while True: #while video is playing
        spec = scene.read()
        frame = scene.read()

        if spec == False:
            scene.release()
            print("Frames saved!")
            break

        cv2.imwrite(f"{save_path}/{count}.png", frame)

        count += 1


def new_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print(f"New directory created: {path}")




if __name__ == "__main__":
    save_folder = "save"    #this is where our frames will be saved
    vid_folder = glob("bloodflow_video/*")  # this is the folder containing the blood cell videos

for path in vid_folder:
    save_frame(path, save_folder)
