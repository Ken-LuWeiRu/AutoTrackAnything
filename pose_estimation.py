import os
import torch
from ultralytics import YOLO
from config import DEVICE, KEYPOINTS

if DEVICE != 'cpu' and torch.cuda.device_count() > 1:
    os.environ['CUDA_VISIBLE_DEVICES'] = DEVICE

class Yolov8PoseModel:
    def __init__(self, device: str, person_conf: float):
        # Ensure this model file is correctly named and available
        # self.model = YOLO('./myModel/yolov8l-face.pt')
        # self.model = YOLO('./myModel/yolov8l-pose.pt')
        # self.model = YOLO('best_person_10epochs.pt')

        # self.model = YOLO('8n_visiblebox.pt')
        self.model = YOLO('./myModel/visible_body_8l_epoch100_best.pt')
        # self.model = YOLO('./myModel/head_8n_best.pt')
        # Use this for filtering detections based on confidence
        self.person_conf = person_conf

    def run_inference(self, image):
        results = self.model(image)
        return results

    def get_filtered_bboxes_by_confidence(self, image):
        results = self.run_inference(image)

        conf_filtered_bboxes = []

        for result in results:
            boxes = result.boxes.cpu().numpy()
            for box in boxes:
                if box.conf[0] > self.person_conf:  # Filter based on confidence
                    conf_filtered_bboxes.append(box.xyxy[0].astype(int))
        print(conf_filtered_bboxes)
        return conf_filtered_bboxes
