#!/usr/bin/env python
import torch

# Model
model = torch.hub.load('/home/ubuntu/yolov5', 'custom', '/home/ubuntu/yolov5/yolov5n_openvino_model', source='local')     # OpenVINO
# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.