from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np

import os
import cv2
#from moviepy.editor import *

fps = 10


def create_rep():
    if not os.path.exists('image_frames'):
        os.makedirs("image_frames")

def generate_frames(test_video_path):
    test_video = cv2.VideoCapture(test_video_path)
    index = 0
    frame_counter = 0
    while test_video.isOpened():
        ret, frame = test_video.read()
        if not ret:
            break
        if frame_counter == index*fps:
            name = './image_frames/frame' + str(frame_counter) + '.png'
            print("Ramka nr... "+str(frame_counter))
            cv2.imwrite(name, frame)
            index = index + 1
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        frame_counter = frame_counter + 1

def main():
    video_path = "videos/traffic.mp4"
    create_rep()
    generate_frames(video_path)
    # print(get_duration(video_path))

main()
