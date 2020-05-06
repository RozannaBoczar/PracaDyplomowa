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


def detect():
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath("models/resnet50_coco_best_v2.0.1.h5")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image="images/image2.jpg", output_image_path="images/image1.jpg",
                                                 minimum_percentage_probability=90)


detect()


