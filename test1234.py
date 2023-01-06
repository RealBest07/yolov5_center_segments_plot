import cv2
import numpy as np
import sys
import glob

import time
import torch
model = model = torch.hub.load('ultralytics/yolov5','yolov5s-seg', force_reload=True)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
