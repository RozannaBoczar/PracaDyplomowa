from imageai.Prediction import ImagePrediction
import os
from imageai.Detection import ObjectDetection

execution_path = os.getcwd()


def predict():
    prediction = ImagePrediction()
    prediction.setModelTypeAsResNet()
    prediction.setModelPath(os.path.join(execution_path, 'models/resnet50_weights_tf_dim_ordering_tf_kernels.h5'))
    prediction.loadModel()
    predictions, probabilities = prediction.predictImage("images/image2.jpg", result_count=1)
    print(predictions)
    print(probabilities)


def detect_car(image, index):  # detect motor, detect truck
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("models/resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    # perfect :3
    detections, extracted_objects = detector.detectObjectsFromImage(input_image=image,
                                                                 output_image_path="image_frames_detected/image" + str(
                                                                     index) + ".png",
                                                                 output_type='file',
                                                                 extract_detected_objects=True,
                                                                 minimum_percentage_probability=80)
    print(detections)
    types = "types of cars, motors etc."
    return types, extracted_objects  # array


def detect_registration(image, index):
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("registration model")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=image,
                                                 output_image_path="image_frames_detected/image" + str(index) + ".png",
                                                 output_type='array',
                                                 extract_detected_objects=True,
                                                 minimum_percentage_probability=80)


detect_car('image_frames/frame50.png', 69)
