from imageai.Detection import VideoObjectDetection
import os
execution_path = os.getcwd()


def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    print("SECOND : ", second_number)
    print("Array for the outputs of each frame ", output_arrays)
    print("Array for output count for unique objects in each frame : ", count_arrays)
    print("Output average count for unique objects in the last second: ", average_output_count)
    print("------------END OF A SECOND --------------")


def detect():
    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("models/resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "videos/cut.mp4"),
                                                 output_file_path=os.path.join(execution_path, "cut_detected")
                                                 , frames_per_second=5, log_progress=True, per_second_function=forSeconds)

    print(video_path)


detect()

