import json

from PIL import Image
import pytesseract
from wand.image import Image as Img
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
import numpy as np
import ImageAIEx
import os
import cv2
# from moviepy.editor import *
import VideoObjectDetection

fps = 10  # take every 10th frame


def create_rep():
    if not os.path.exists('image_frames'):
        os.makedirs("image_frames")


# the idea below died XD oh no we have to come back here :) maybe.... XD!
def generate_frames(test_video_path):
    result = "json file"
    test_video = cv2.VideoCapture(test_video_path)
    index = 0
    frame_counter = 0
    while test_video.isOpened():
        ret, frame = test_video.read()
        if not ret:
            break
        if frame_counter == index * fps:
            name = './image_frames/frame' + str(frame_counter) + '.png'
            print("Ramka nr... " + str(frame_counter))
            cv2.imwrite(name, frame)
            index = index + 1
            types, extracted_images = ImageAIEx.detect_car(name, frame_counter)
            # i w sumie na tej ramke mozna cos robic
            for car_type, cars in types, extracted_images:
                registration = registration_detection(cars)
                brand = brand_detection(cars)
                res = prepare_result(registration, brand, type)
                # dopisz res do result
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        frame_counter = frame_counter + 1
    return result

def detect_cars(video_path):
    VideoObjectDetection.detect(video_path)


def registration_detection(car_image):
    pass


def brand_detection(car_image):
    pass


# result in json <3 reg, brand, type
def prepare_result(*args):
    result = {
        'registration': args[0],
        'brand': args[1],
        'type': args[2]
    }
    result = json.dumps(result)
    return result


def main():
    video_path = "videos/cut.mp4"
    create_rep()
    detect_cars(video_path)
    # generate_frames(video_path)
    # print(get_duration(video_path))


main()
