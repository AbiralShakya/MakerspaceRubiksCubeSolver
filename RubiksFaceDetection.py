import cv2 
import numpy as np


class ColorDetection:
    def __init__(self):
        self.prominent_color_palete = {
            'red': (0,0,255),
            'orange': (0,165, 255),
            'blue' : (255, 0, 0),
            'green': (0,255,0),
            'white': (255, 255, 255),
            'yellow': (0,255,255)
        }